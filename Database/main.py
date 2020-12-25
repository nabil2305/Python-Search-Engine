import mysql.connector


class Database:
    mydb = mysql.connector.connect(
        host="localhost",
        user="nabil",
        password="nabil",
        database="mydatabase"
    )
    mycursor = mydb.cursor()
    #mycursor.execute("CREATE TABLE loc23(name VARCHAR(255),location VARCHAR(255))")

    def insert(self, mylist1, file_name):
        print("filename")
        print(file_name)
        # mycursor = Database.mydb.cursor()
        # mycursor.execute("CREATE TABLE loc4 (location VARCHAR(255))")
        sql = "INSERT INTO loc23 (name,location) VALUES (%s,%s)"
        for val in mylist1:
            val1 = [(file_name),(val)]
            val2=tuple(val1)
            Database.mycursor.execute(sql, val2)
        Database.mydb.commit()
        print( "records are  inserted.")

    def query(self,file_name):
        symbol=file_name
        Database.mycursor.execute("SELECT location FROM loc23 WHERE name LIKE %s", (symbol,))
        myresult = Database.mycursor.fetchall()
        query_length=len(myresult)
        if(query_length>0):
            for x in myresult:
                print("Query from database")
                print(x)
        return query_length

