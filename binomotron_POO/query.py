import mysql.connector

class Query:

    def __init__(self):
        self.mydb = mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "binomotron",
            )
        self.cursor = mydb.cursor

    def get_apprenants(self):
        array = list()
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "binomotron",
            )
        cursor = mydb.cursor()
        cursor.execute("SELECT prenom FROM apprenants")
        for ligne in cursor.fetchall():
            array.append(ligne[0])
        mydb.close
        return(array)


    def add_crew(self):
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "binomotron",
            )
        cursor = db.cursor()
        sql = """INSERT INTO apprenant_groupe(id_groupe, id_binome, id_project)
        VALUES (10 ,20, 10)"""
        cursor.execute(sql)
        # Commit your changes in the database
        db.commit()
        db.close()
Query().get_apprenants()
