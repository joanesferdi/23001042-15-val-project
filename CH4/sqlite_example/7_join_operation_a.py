import sqlite3

from datetime import datetime
dtm = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

conn = sqlite3.connect('data/binar_data_science_join.db')
print("Opened database successfully")

conn.execute('''DROP TABLE IF EXISTS users''')
conn.execute('''CREATE TABLE users (username varchar(255), email varchar(255));''')
print("Table 'users' created successfully")

success_message = f"{dtm} - create table users complete!"
with open("../log/database_proccess.txt", "a", encoding = 'latin') as log_file:
    log_file.write(success_message + "\n")

conn.execute('''INSERT INTO users (username, email) VALUES 
             ('bowo', 'bowo@binar.com'), 
             ('kiky', 'kiky@binar.com'), 
             ('faza', 'faza@binar.com'),
             ('jovanca', 'jovanca@binar.com')
             ''')
print("Insert to Table 'users' is successfully")

conn.execute('''DROP TABLE IF EXISTS hobbies''')
conn.execute('''CREATE TABLE hobbies (name varchar(255), user_id INT, FOREIGN KEY (user_id) REFERENCES users(rowid));''')
print("Table 'hobbies' created successfully")
success_message = f"{dtm} - create table hobbies complete!"
with open("../log/database_proccess.txt", "a", encoding = 'latin') as log_file:
    log_file.write(success_message + "\n")

# checkpoint
conn.execute("INSERT INTO hobbies (name, user_id) VALUES ('football', 1);")
conn.execute("INSERT INTO hobbies (name, user_id) VALUES ('gaming', 2);")
conn.execute("INSERT INTO hobbies (name, user_id) VALUES ('traveling', 2)")
print("Insert to Table 'hobbies' is successfully")

conn.commit()
print("Records created successfully")
conn.close()