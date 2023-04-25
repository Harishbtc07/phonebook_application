from dao.Propertyfile.dbconnection import connection
import logging
logging.basicConfig(filename='C:\\Users\\Harish Reddy\\PycharmProjects\\phonebook application\\dao\\service\\log.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
class findjunk:
    '''this method will fetch mobile_no that contains
     special characters in it and ask the user to if
     the want delete from database or what.'''
    @staticmethod
    def find():
            logging.info("\nfinding the number which contains a special charactes")
            cur=connection.conn.cursor()
            sql="select * from PhoneBook where Mobile_no Regexp '[^0-9]'"
            cur.execute(sql)
            records = cur.fetchall()
            print("\nPrinting each row")
            for row in records:

                print("Name = ", row[1], )
                print("Mobile_no = ", row[2],"\n")

            delete=input("do You want delete user from data base (Y/N):")
            if delete=="y" or delete=='Y':

                sql="delete from PhoneBook where User_id={}".format(row[0])
                print(row[1],"deleted from databse")
                cur.execute(sql)
                connection.conn.commit()
                print("succesful")
            elif delete=='N' or delete=='n':
                print("ok")


#findjunk.find()



