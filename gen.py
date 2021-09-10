import os, sys, argparse, datetime
import json
import jinja2

DEFAULT_DATA_FILE = 'data.json'
DEFAULT_TEMPLATE_FILE = 'basic.html.j2'
DEFAULT_TARGET_FILE = 'statuspages.html'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', type=str, default=DEFAULT_DATA_FILE, required=False)

    args = parser.parse_args()

    # Read data
    with open(args.data, 'rt') as dataFile:
        contentDataJson = json.loads(dataFile.read())

    for pageKey, pageDataJson in contentDataJson.items():
        j2TemplateFile = DEFAULT_TEMPLATE_FILE
        targetHtmlFile = DEFAULT_TARGET_FILE
        if 'config' in pageDataJson:
            if 'template' in pageDataJson['config']:
                j2TemplateFile = pageDataJson['config']['template']
            if 'target' in pageDataJson['config']:
                targetHtmlFile = pageDataJson['config']['target']

        # Order cards
        pageDataJson['cards'] = dict(sorted(pageDataJson['cards'].items(), key=lambda item: item[0]))

        # Associate service with cards
        for serviceKey, serviceData in pageDataJson['services'].items():
            if not serviceData['card'] in pageDataJson['cards']:
                continue
            if not 'data' in pageDataJson['cards'][serviceData['card']]:
                pageDataJson['cards'][serviceData['card']]['data'] = []
            pageDataJson['cards'][serviceData['card']]['data'].append(serviceData)

        pageDataJson['datetime'] = datetime.datetime.now()

        # Read template
        if not os.path.exists(j2TemplateFile):
            print("Template file doesn't exist")
            sys.exit(1)
        with open(j2TemplateFile, 'rt') as j2TemplateFile:
            contentTemplate = j2TemplateFile.read()

        # Generate status pages
        j2Template = jinja2.Template(contentTemplate)
        j2TemplateRendering = j2Template.render(pageDataJson)

        # Write HTML status page (rendered)
        with open(targetHtmlFile, 'wt') as statusPageFile:
            statusPageFile.write(j2TemplateRendering)
