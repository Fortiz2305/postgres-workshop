# postgres-workshop
This repository contains code related to a PostgreSQL workshop.

## bulkload
Using the following [data](https://www.capitalbikeshare.com/system-data) for 2015-Q2. Files can be downloaded from [here](https://s3.amazonaws.com/capitalbikeshare-data/index.html). We are going to show 4 different approaches to bulk data into PostgreSQL database in python.
* line by line
* Using Prepared Statements
* Batch insertion
* Using [COPY](https://www.postgresql.org/docs/current/static/sql-copy.html) command of postgresql
