import mysql.connector
from mysql.connector import Error
import pandas as pd
import functions as f

pw = input("Enter your MySQL password: ")
db = input("Enter your MySQL database name: ")

connection = f.create_server_connection("localhost", "root", pw)
create_db_query = f"CREATE DATABASE IF NOT EXISTS {db}"
f.create_database(connection, create_db_query)

create_teacher_table = """
CREATE TABLE IF NOT EXISTS teacher (
  teacher_id INT PRIMARY KEY,
  first_name VARCHAR(40) NOT NULL,
  last_name VARCHAR(40) NOT NULL,
  language_1 VARCHAR(3) NOT NULL,
  language_2 VARCHAR(3),
  dob DATE,
  tax_id INT UNIQUE,
  phone_no VARCHAR(20)
  );
 """
connection = f.create_db_connection("localhost", "root", pw, db) # Connect to the Database
f.execute_query(connection, create_teacher_table) # Execute our defined query


