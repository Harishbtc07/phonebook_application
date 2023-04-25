from dao.Propertyfile.dbconnection import connection
import logging
import dao.display as d
logging.basicConfig(filename='C:\\Users\\Harish Reddy\\PycharmProjects\\phonebook application\\dao\\service\\log.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

class delete:
    '''here we are we calling display function and from we are
     asking to pick one user id based on user id based
     on user input we are deleting user from the database'''
    @staticmethod
    def remove():
        cur = connection.conn.cursor()
        d.display.disp()
        name=(input("Enter the name to delete from db:"))


        sql = f"delete from PhoneBook where Name='{name}'"

        cur.execute(sql)
        connection.conn.commit()
        print("Succesfully deleted from Storage")

        logging.info("succesfully deleted")
#delete.remove()