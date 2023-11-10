import sqlite3

conn = sqlite3.connect('data/binar_data_science.db')
print("Opened database successfully")
print()

print("List of Users:")
cursor = conn.execute("SELECT * FROM users WHERE umur = 30;")

# mas faza done
"SELECT * FROM users WHERE umur = 30;"

# mas kiki & mas azis
'''SELECT *
FROM user
WHERE  umur = '30'''

# mba claire done
#cursor = conn.execute("SELECT * FROM users WHERE umur = 30;")

for baris in cursor:
    print(baris)

print()
print("Operation done successfully")
conn.close()