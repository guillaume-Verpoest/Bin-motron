import mysql.connector
people = list()
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "binomotron",
    )
cursor = mydb.cursor()
cursor.execute("SELECT prenom FROM apprenants")
rows = cursor.fetchall()
for row in rows:
  people.append(row[0])
mydb.close
print(people)


print(%s),2