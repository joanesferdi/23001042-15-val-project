import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")

conn.execute("INSERT INTO users (username, email, umur, alamat) VALUES ('binaria', 'binaria@binar.com', 30, 'jakarta barat')")

conn.execute("INSERT INTO users VALUES ('bintang', 'bintang@binar.com', 30, 'Bandung')")
conn.execute("INSERT INTO users VALUES ('kiky', 'kiky@binar.com', 28, 'Bandung')")

conn.commit()
print("Records created successfully")
conn.close()
