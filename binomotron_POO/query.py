import mysql.connector

class Query:

    def __init__(self):
        pass

    def get_apprenants(self):
        array = list()
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "root",
            database = "binomotron",
            )
        cursor = mydb.cursor()
        cursor.execute("SELECT id_apprenants FROM apprenants")
        for ligne in cursor.fetchall():
            array.append(ligne[0])
        mydb.close
        return(array)


    def add_crew(self, crew):
        pass
Query().get_apprenants()
#Query().add_crew()
