# Log-Analysis

Logs Analysis Project, Part of the Udacity [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## What it is and does:

A Reporting page that prints out reports in a plain text format based on the data in the database. This reporting tool is a python program using the `psycopg2` module to connect to the database.

## Questions:

1. What are the most popular three aricles of all time?
   
2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?
   

## Software Requirements

* Python
* VirtualBox
* Vagrant
* Git
* PostgreSQL

## Contents

In this project consists for following files:

* log_analysis.py - It is a main file to run Logs Analysis Reporting Tool

* logs_output.txt - It is a output file that will shown on the git bash

* README.md - It is an Instructions to install this reporting tool

## Installation

There are some urls and a few instructions on how to run the project

## URL's

- [Git](https://git-scm.com/downloads)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/)

## Installation Process

* Install Git, VirtualBox and Vagrant
* vagrant  init to create vagrant file 
* Then vagrant up  to download and to bring  the vm up
* vagrant ssh to  connect to the vm from windows terminal

## How to Run Project

Download the project zip file and unzip the file now copy unzip file inside `vagrant/Log-Analysis`

1. Launch the Vagrant VM inside Vagrant sub-directory in the downloaded fullstack-nanodegree-vm repository using command.

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
8. Create the views using the following sql quieries after connecting to news database

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

## Miscellaneous
This project is inspiration from [saral](https://github.com/SaralKumarKaviti/Log-Analysis)
