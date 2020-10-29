import mysql.connector

class Query:

    def get_apprenants(self):
        array = list()
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "binomotron",
            )
        cursor = mydb.cursor()
        cursor.execute("SELECT nom FROM apprenants")
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
        sql = """INSERT INTO apprenant_groupe(id_apprenants, id_projet, id_groupe)
        VALUES (1 ,1, 1)"""
        cursor.execute(sql)
        db.commit()
        db.close()

Query().get_apprenants()
#Query().add_crew()
