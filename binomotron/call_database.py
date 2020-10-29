import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "binomotron",
    )
cursor = mydb.cursor()
cursor.execute("INSERT INTO groupe (id_groupe, libelle_groupe) VALUES (%s, %s)", ("NULL", "groupe20"))
cursor.commit()
cursor.close()
