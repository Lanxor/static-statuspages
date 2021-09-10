# Static-StatusPages

Static status page generator.

The objective of this project is to be able to dissociate asynchronously the generation of the HTML page and the execution of the supervision command.

This project is mainly based on the work of **Cyclenerd** available on the following repository : https://github.com/Cyclenerd/static_status.

* **Simple**: Use python and jinja templating to generate HTML pages.
* **Static**: No backend, access on automation (without human intervention).
* **Lightweight**: No strong dependencies or specific language. Create static HTML pages
* **Flexible**: All informations is on Json file.
* **Customize**: HTML templating with jinja

# Principes

The goal is that the supervision continuously modifies the data file and recurrently the HTML status page is generated.

A status page has a template with several types of blocks (or cards).
Each service can be attached to a card to compartmentalize the different information. The cards can represent products (marketplace, backend, etc.) or states (outage, operational, etc.), depends on you.

# Requirements

Script developed from the following versions:

* Python 3.9.2
* Jinja2-3.0.1

## Python modules installation

```
python3 -m pip install jinja2
```

# Examples

```
git clone https://github.com/Lanxor/static-statuspages.git
cd static-statuspages
python3 gen.py --data examples/example01.json
```

You can open the generated HTML file: *statuspages.html*

## Add new service status with cli-service.py

```
cp examples/example01.json testdata.json
python3 cli-service.py --data testdata.json --page page1 --service 'Webservice 02' --status 'ok' --card 0 --information 'webservice is running'
python3 gen.py --data testdata.json
```

You can open the generated HTML file: *statuspages.html*

## Changes the status of an incident

```
cp examples/example03.json testdata.json
python3 cli-service.py --data testdata.json --page page1 --service-id 2 --status 'ok' --card 2 --information 'access granted'
python3 gen.py --data testdata.json
```

You can open the generated HTML file: *statuspages.html*

# Todo

* Add monitoring exemples/scripts/modules which update JSON file
* Dynamic menu to navigate between pages (different presentation)
* Add other complex card (ex: tables)
* Improve CLI-service to update JSON file services
* Add CLI scripts to update more data in JSON file
* Add other HTML template

# Licence

GNU Public License version 3.
