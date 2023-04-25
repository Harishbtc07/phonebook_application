from dao.Propertyfile.dbconnection import connection

class display:
    #Displying re
    @staticmethod
    # below method will fetch the deails based on the user input we used limit to stop being fetch all the records from DB
    def disp():

            cur=connection.conn.cursor()

            id=int(input("How many records you want fetch:"))
            cur.execute("select * from PhoneBook  limit {}".format(id))
            records = cur.fetchall()
            print("Total number of rows in table: ",cur.rowcount)
            print("Printing each row")
            for x in records:
                print(x)

#display.disp()