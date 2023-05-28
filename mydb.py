import environ

import mysql.connector

env = environ.Env()
environ.Env.read_env()

database = mysql.connector.connect(
    host='localhost',
    user=env('DB_USER'),
    password=env('DB_PWD'),
)

# Prepare a cursor object
cursorObject = database.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE crmdb")
