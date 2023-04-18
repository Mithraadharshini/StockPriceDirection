import mysql.connector
class DBConnection:
    @staticmethod
    def getConnection():
        
        print("****************************")
        print("DBConnection")
        print("****************************")
        database = mysql.connector.connect(host="localhost", user="root", password="", db='stocks')
        return database
if __name__=="__main__":
    print(DBConnection.getConnection())