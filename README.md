# postgres-workshop
This repository contains code related to a PostgreSQL workshop.

## bulkload
Using the following [data](https://www.capitalbikeshare.com/system-data) for 2015-Q2. Files can be downloaded from [here](https://s3.amazonaws.com/capitalbikeshare-data/index.html). We are going to show 4 different approaches to bulk data into PostgreSQL database in python.
* line by line
* Using Prepared Statements
* Batch insertion
* Using [COPY](https://www.postgresql.org/docs/current/static/sql-copy.html) command of postgresql

## Export tables into CSV

Using a 500k rows table, we are going to try exporting files using the different approaches:

  * Line by Line
  * Line by Line using JSON format.
  * Using the COPY command.

NOTE: this can be done using the same data that we used in the bulkload part.
