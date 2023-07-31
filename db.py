import mysql.connector as mys
f = open('sql.txt','r')
sql = f.read()
sqlx = sql.split(',')
hostx = sqlx[0]
userx = sqlx[1]
passwdx = sqlx[2]
conn = mys.connect(host = hostx, user = userx, passwd = 'ashmitiscool')
cursor = conn.cursor()
