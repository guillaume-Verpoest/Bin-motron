import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "root",
    database = "binomotron",
    )
cursor = mydb.cursor()
cursor.execute("INSERT INTO groupe (id_groupe, libelle_groupe) VALUES (NULL,'Groupe3')");
cursor.execute("INSERT INTO groupe (id_groupe, libelle_groupe) VALUE (NULL, 'Groupe5'), (NULL, 'Groupe6'), (NULL, 'Groupe7'), (NULL, 'Groupe8'), (NULL, 'Groupe8'), (NULL, 'Groupe9'), (NULL, 'Groupe10')")
cursor.close()
