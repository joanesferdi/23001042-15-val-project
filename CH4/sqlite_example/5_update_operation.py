import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")
print()

conn.execute("UPDATE users SET alamat = 'Jaktim' where username = 'binaria';")
conn.commit()

# mba claire done
# conn.execute("UPDATE users SET alamat = 'jaktim' where alamat = 'jakarta timur';")

# mas faza done
# "UPDATE users SET alamat = 'jaktim' where alamat = 'jakarta timur';"

# kang toni 
# conn.execute("UPDATE users SET alamat = 'jaktim' where username = 'Jakarta timur';")

# mas ghiyats done
# conn.execute("UPDATE users SET alamat = 'jaktim' where alamat = 'jakarta timur';")

# mas azis
# ("update users set alamat = 'Jaktim' where alamat = 'Jakarta Timur';")

# mas bathis
# "UPDATE users SET alamat = 'Jaktim' where username = 'binaria';"

print("List of Users:")
cursor = conn.execute("SELECT * FROM users;")
for row in cursor:
    print(row)

print()
print("Operation done successfully")
conn.close()

