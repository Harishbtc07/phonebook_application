import logging

import mysql
logging.basicConfig(filename='C:\\Users\\Harish Reddy\\PycharmProjects\\phonebook application\\dao\\service\\log.txt',
                            filemode='a',
                            format='%(asctime)s, %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
from dao.Propertyfile.dbconnection import connection
class search:
    #we created two methods one searches by name and other
    # one searches by number
    @staticmethod
    def searchByname():
        try:

            logging.info(":Searching by name")
            Nam = input("Enter the Name You want to search:")
            '''below line will return true O false if Nam 
             contains both alphabet and number it will 
            retrun true otherwise it will print false'''
            if  Nam.isalnum():
                cur = connection.conn.cursor()
                sql = "select * from PhoneBook where Name like'%{}%' Limit 2".format(Nam)
                cur.execute(sql)
                records = cur.fetchall()
                print("Total number of rows in table: ", cur.rowcount)
                print("here the details you are looking for:")
                if records==None:
                        print("There is no matching details found")
                else:
                    for row in records:

                        print("\nName = ", row[1] )
                        print("Mobile_no = ", row[2],"\n")
            else:
                print("please enter numbers and character")

        except mysql.connector.Error as e:
                logging.error("Error reading data from MySQL table", e)


    @staticmethod
    def searchByNumber():
        try:
            logging.info(":Searching by mobile number")
            Num = input("Enter the number You want to search:")
            if Num.isdigit():
                cur = connection.conn.cursor()
                sql = "select * from PhoneBook where Mobile_no like'{}%'".format(Num)
                cur.execute(sql)
                #cursor.fetchall() fetches all the rows of a query result.
                # It returns all the rows as a list of tuples.
                # An empty list is returned if there is no record to fetch.
                records = cur.fetchall()
                print("Total number of rows in table: ", cur.rowcount)
                print("\nPrinting each row")
                if records == None:
                    print("There is no matching details found")
                else:
                    for row in records:
                        print("\nName", row[1])
                        print("Mobile_no = ", row[2],"\n" )
            else:
                logging.info("please provide a number")
        except mysql.connector.Error as e:
                print("Error reading data from MySQL table", e)
#search.searchByname()


