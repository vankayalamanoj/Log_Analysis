#! /usr/bin/env python
import psycopg2

# Connection to the  plsql database with credentials
try:
    connection = psycopg2.connect(database="news",
                                  user="vagrant",
                                  password="12345",
                                  host="127.0.0.1",
                                  port="5432")
except psycopg2.DatabaseError, e:
    print("Unable to connect to database")
cur_object = connection.cursor()


# Function to display the error rate greater than 1


def err_Rate():
    ''' It is a function to  print error rate
    and date on which error rate is more than  one percent '''
    print '\nError Rate:\n'
    myQry = '''select total.date, round(fail.f_cnt*100.00/total.t_cnt, 2)
    as Rate
    from Fail_Count fail inner join Tot_Count total on fail.date = total.date
    where fail.f_cnt*100.00/total.t_cnt > 1 ; '''
    result = cur_object.execute(myQry)
    rows = cur_object.fetchall()
    for val in rows:
        print val[0], '--->', val[1], '%', 'errors\n'

# Function To display the popular three articles with their views


def pop_Art():
    ''' Its is a function to print the most popular
    articles of all the time from the news database'''
    print '\nPopular Articles:\n'
    myQ = '''select art.title, count(art.slug) as views
    from articles art inner join log log on art.slug =
    replace(log.path, '/article/', '')
    where log.status = '200 OK' and log.path != '/'
    group by log.path, art.title
    order by count(log.path) Desc limit(3);'''
    result = cur_object.execute(myQ)
    rows = cur_object.fetchall()
    for val in rows:
        print val[0], '--->', val[1], '\n'
    print '-------------------------------------------------------------'

# Function to display popular authors with their article views


def pop_Auth():
    ''' It is a function to print popular author
    of all time based on the views in logs table '''
    print '\nPopular Authors:\n'
    myQry = '''select name, sum(rqts) as tot_art_vws
    from keysnrqst kyrst inner join articles art on art.slug = kyrst.ky
    inner join authors auth on auth.id = art.author
    group by name
    order by tot_art_vws Desc;'''
    result = cur_object.execute(myQry)
    rows = cur_object.fetchall()
    for val in rows:
        print val[0], '--->', val[1], '\n'
    print '------------------------------------------------------------'

if __name__ == '__main__':
    pop_Art()
    pop_Auth()
    err_Rate()
    cur_object.close()
    connection.close()
