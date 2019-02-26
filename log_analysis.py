import psycopg2


connection = psycopg2.connect(database="news",
                        user="vagrant",
                        password="12345",
                        host="127.0.0.1",
                        port="5432")
cur_object = connection.cursor()


def pop_Art():
    print '\nPopular Articles:\n'
    '''Function To display the popular three articles with their views'''
    myQuery = '''select art.title, count(art.slug) as views
    from articles art inner join log log on art.slug =
    replace(log.path, '/article/', '')
    where log.status = '200 OK' and log.path != '/'
    group by log.path, art.title
    order by count(log.path) Desc limit(3);'''
    result = cur_object.execute(myQuery)
    rows = cur_object.fetchall()
    for value in rows:
        print value[0], '--->', value[1], '\n'
    print '------------------------------------------------------------'


def pop_Auth():
    ''' Function to display popular authors with their article views '''
    print '\nPopular Authors:\n'
    myQuery = '''select name, sum(rqts) as tot_art_vws
    from keysnrqst kyrst inner join articles art on art.slug = kyrst.ky
    inner join authors auth on auth.id = art.author
    group by name
    order by tot_art_vws Desc;'''
    result = cur_object.execute(myQuery)
    rows = cur_object.fetchall()
    for value in rows:
        print value[0], '--->', value[1], '\n'
    print '------------------------------------------------------------'


def err_Rate():
    ''' Function to display the error rate greater than 1 '''
    print '\nError Rate:\n'
    myQuery = '''select total.date, round(fail.f_cnt*100.00/total.t_cnt, 2)
    as Rate
    from Fail_Count fail inner join Tot_Count total on fail.date = total.date
    where fail.f_cnt*100.00/total.t_cnt > 1 ; '''
    result = cur_object.execute(myQuery)
    rows = cur_object.fetchall()
    for value in rows:
        print value[0], '--->', value[1], '%', 'errors\n'
pop_Art()
pop_Auth()
err_Rate()
cur_object.close()
connection.close()
