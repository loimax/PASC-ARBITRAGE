import mysql.connector
from mysql.connector import Error
import pandas as pd
import functions as f

connection = f.create_server_connection("localhost", "root", "Maxence")
f.create_database(connection, "CREATE DATABASE IF NOT EXISTS testdb")

create_teacher_table = """
CREATE TABLE teacher (
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

connection = f.create_db_connection("localhost", "root", "testdb") # Connect to the Database
f.execute_query(connection, create_teacher_table) # Execute our defined query

