import mysql.connector
people = list()
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "binomotron",
    )

cursor = mydb.cursor()


cursor.execute("INSERT INTO groupe (id_groupe, libelle_groupe) VALUES (21, 'Groupe55'), (22, 'Groupe66')")

cursor.close()
cursor = mydb.cursor()
#cursor.execute("SELECT prenom FROM apprenants")
cursor.close()

# import mysql.connector
# array = list()
# mydb = mysql.connector.connect(
#     host = "localhost",
#     user = "root",
#     password = "root",
#     database = "binomotron",
#     )
# cursor = mydb.cursor()
# cursor.execute("SELECT  FROM groupe")
# for ligne in cursor.fetchall():
#   array.append(ligne)
# mydb.close
# print(array)