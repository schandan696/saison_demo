# Saison Omni Coding
## _SEACHE a highly optimise seaching app_
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

SEACHE is a cloud-enabled, Python powered application.

- Python
- Flask
- AWS
- EC2
- PostgreSQL
- GIS
- GitHub

## Features

- [x] Search by name of applicant.
- [x] Search by expiration date, to find whose permits have expired.
- [x] Search by street name.
- [x] Add new food truck entry to the dataset.
- [x] Given a delivery location, find out the closest truck possible.

## Installation

SEACHE requires [Python](https://www.python.org/downloads/) v3+ to run.

Install the dependencies and devDependencies and start the server.

```sh
cd project_folder
pip install -r requirements.txt
python app.py
```
## Assumptions & Disclaimer 
- Assuming street name should be search by address and location discription not from lognitude and lattiude   
- I have't added any data vaildiation (Demo)
- Using Postgres Text search Simalirity and GIS feature it's soetime not that accurate.
- Haven't added nGinex or something to proxy pass and open 3000 port so less secure
- More on the go indexing so beacuse of less dataets
- Performance less than 10ms for all API 
