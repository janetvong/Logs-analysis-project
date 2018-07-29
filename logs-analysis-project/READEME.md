# Logs Analysis Project (Udacity Course)

The Logs Analysis Project is an internal reporting tool that uses information from the `news.sql` database to help you have a better understanding of which articles are liked by the site's readers.

## Prerequisite

*   You'll need a basic understanding of how to use the command line so that you can run the code in your terminal.
*   You'll need a database software (provided by a Linux virtual machine) and data to analyze.
*   You'll need to install the virual machine to use PostgreSQL database and support software needed for this project.


## Background

The `news.sql` database consists of three tables: articles, authors, and logs. These tables contain information on newspaper articles, and web server logs for the site. The log has a database row for each time a reader loaded a web page.

This project will help us answer three questions about the site's user activity:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

To answer these questions, the tables are joined together to display all of the necessary fields to answer the questions.

## Design (of the code / source code)

In the source code, the libraries `sqlite3` and `psycopg2` are imported.

Next, the `psycopg2` module connects to the database `news`, which runs PostgreSQL. The database is called `db`.

The cursor class is called so that the database `db` is bound to the connection for the entire lifetime, and all commands that are executed in the context of the database sesson wrapped by the connection.

Next, there are three SQL queries for answering the three questions, which are requirements for this project.

1.) What are the most popular three articles of all time?
*   The SQL query joins the articles and log tables to display the article's title and number of logs for those articles. The counts are grouped by article, ordered by the number of logs, and displays the top three results.

2.) Who are the most popular article authors of all time?
*   The SQL query joins all three tables and displays the author's name, and the count of the log paths, grouped by the author's names, and ordered by the log path.


3.) On which days did more than 1% of requests lead to errors?
*   The SQL query uses the log table to display the days, and the number of times where there was an error each day. The query also displays the total number of logs per day, and computes a ratio errors/total. The output is grouped by day.

The query results are fetched and stored into a variable result1, result2, or result3, depending on the question.

Lastly, the cursor is closed when the is done executing.

## How to run the program
1. In your terminal, bring up the virtual machine with the command `vagrant up`.
2. Log into the virtual machine with `vagrant ssh`.
3. Download the `newsdata.sql` data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
4. Move the `newsdata.sql` file into your `vagrant` directory.
5. Load the data with the following command `psql -d news -f newsdata.sql`.
6. Download the `code.py` file and move the file into your `vagrant` directory.
7. Type `python code.py` and the output will show the answers to the three questions.