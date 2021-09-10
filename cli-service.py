import os, sys, argparse
import json

DEFAULT_DATA_FILE = 'data.json'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--data', type=str, default=DEFAULT_DATA_FILE)
    parser.add_argument('--page', type=str)
    parser.add_argument('--service-id', type=str, dest='serviceId')
    parser.add_argument('--service', type=str)
    parser.add_argument('--status', choices=['ok', 'OK', 'ko', 'KO'])
    parser.add_argument('--information', type=str)
    parser.add_argument('--card', type=str)
    parser.add_argument('--delete', action='store_true')

    args = parser.parse_args()

    # Check arguments
    ## Page required
    if args.page == None:
        print("Error usage\nMissing parameter --page.")
        sys.exit(1)

    if args.serviceId == None and args.service == None:
        print("Error usage\nMissing parameter --service-id or --service")
        sys.exit(1)

    # Read data
    with open(args.data, 'rt') as dataFile:
        contentDataJson = json.loads(dataFile.read())

    if not args.page in contentDataJson:
        print("Error page '{0}' doesn't exist in data file".format(args.page))
        sys.exit(1)

    if args.serviceId != None:
        serviceId = args.serviceId
    else:
        serviceId = args.service

    if args.delete == True:
        if serviceId in contentDataJson[args.page]['services']: del contentDataJson[args.page]['services'][serviceId]
    else:
        if not serviceId in contentDataJson[args.page]['services']:
            contentDataJson[args.page]['services'][serviceId] = {}

        if args.service != None:
            contentDataJson[args.page]['services'][serviceId]['name'] = args.service
        if args.information != None:
            contentDataJson[args.page]['services'][serviceId]['information'] = args.information
        if args.status != None:
            contentDataJson[args.page]['services'][serviceId]['status'] = args.status
        if args.card != None:
            contentDataJson[args.page]['services'][serviceId]['card'] = args.card

    # Write data
    with open(args.data, 'w') as dataFile:
        dataFile.write(json.dumps(contentDataJson, indent=2))
