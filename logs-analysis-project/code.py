import sqlite3
db = psycopg2.connect("dbname=news")
cursor = db.cursor()

# First question
query1 = "SELECT articles.title, count(log.path) FROM articles, log WHERE ('/article/' || articles.slug) = log.path GROUP BY articles.title ORDER BY count(log.path) DESC LIMIT 3;"

cursor.execute(query1)
results1 = cursor.fetchall()

print "1. What are the most popular three articles of all time?"
print results1

# Second question
query2 = "SELECT authors.name, count(log.path) FROM articles, authors, log WHERE articles.author = authors.id AND ('/article/' || articles.slug) = log.path GROUP BY authors.name ORDER BY count(log.path) DESC LIMIT 10;"

cursor.execute(query2)
results2 = cursor.fetchall()

print "2. Who are the most popular article authors of all time?"
print results2

# Third question
query3 = "SELECT date_trunc('day', log.time) AS day, count(status) FILTER (WHERE status NOT LIKE '200 OK') AS errors, count(log.status) AS total, ((count(status) FILTER (WHERE status NOT LIKE '200 OK')) / count(log.status)) AS percentage FROM log GROUP BY day;"

cursor.execute(query3)
results3 = cursor.fetchall()

print "3. On which days did more than 1% of requests lead to errors?"
print results3

db.close()