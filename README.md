# Log-Analysis

Logs Analysis Project, Part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Overview

In this project, we will work with fields representing from web servers such as HTTP's and URL paths. The web servers use the same database allowing the information to flow from the servers into the report.

## What it is and does:

A Reporting page that prints out reports in a plain text format based on the data in the database. This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Questions:

1. What are the most popular three aricles of all time?
   
2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?
   

## Requirements

* Python
* VirtualBox
* Vagrant
* Git
* PostgreSQL

## Contents

Files in this project are:

* log_analysis.py - It is a main file to run Logs Analysis Reporting Tool

* output.txt - It is a output file that will shown on the git bash

* README.md - It is an Instructions to install this reporting tool

## URL's

- Install GIT from [here](https://git-scm.com/downloads)
- Install VirtualBox from [here](https://www.virtualbox.org/wiki/Downloads)
- Install Vagrant from [here](https://www.vagrantup.com/)

## Running Project

Download the project zip file and unzip the file now copy unzip file inside `vagrant/Log-Analysis`

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using the following command.

```
$ vagrant up
```
2. Now log into vagrant using below command

```
$ vagrant ssh
```
3. Download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

4. Unzip downloaded file. The file inside is called newsdata.sql

5. Copy the newsdata.sql file and place inside `vagrant/Log-Analysis` 

6. cd into the correct project directory `vagrant/Log-Analysis`

7. Load the data in local database using the command:

```
$ psql -d news -f newsdata.sql
```
8. Create the views using sql quieries that are mentioned below after connecting to news database

    * Connection to database

    ```
        psql -d news
    ```

    * View to count number of views for a  article from logs table

    ```
    create view keysnrqst as select count(lg.path) as rqts,replace(lg.path, '/article/', '') as ky from articles ar inner join log lg on ar.slug=replace(lg.path, '/article/', '') where lg.status = '200 OK' and lg.path != '/' group by lg.path;
    ```
    * View to count failure requests from logs table in a day

    ```
    create view Fail_Count as select count(date(time)) as f_cnt,date(time) from log where status != '200 OK' group by date(time);
    ```
    * View to count total number of requests in a day

    ```
    create view Tot_Count as select count(date(time)) as t_cnt,date(time) from log where status != '200 OK' or status = '200 OK' group by date(time);
    ```

9. Now run log_analysis.py file 
```
$ python log_analysis.py
```
Note: queries will take sometime to execute
