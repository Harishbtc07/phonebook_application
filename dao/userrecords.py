import re
import mysql
import logging

logging.basicConfig(filename='C:\\Users\\Harish Reddy\\PycharmProjects\\phonebook application\\dao\\service\\log.txt',
                            filemode='a',
                            format='%(asctime)s, %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
from dao.Propertyfile.dbconnection import connection
class user:
    '''create method will save user_id
    ,name,mobile number,field and email into Database
    for valdating phone number and email we used Regex
     RegEx, or Regular Expression, is a sequence of characters that forms a
     search pattern.RegEx can be used to check if a string contains the
     specified search pattern.'''

    @staticmethod

    def create_record():

        '''A cursor is an object which helps to execute the
        query and fetch the records from the database. The
         cursor plays a very important role in executing the query'''
        try:
            m = connection.mycursor
            ''' Here we used isalpha and isalnum to validate user input'''

            name=input("Enter Name To Save:")
            if  not name.isalnum():
                        #Logger.info(msg) : This will log a message with level INFO on this logger.
                        logging.info("This is"+name+" invalid name Please enter name using numbers and characters")
                        print("This is"+name+" invalid name Please enter name using numbers and characters")

                            # try:
                            #     raise Exception("Please enter name using numbers and characters")
                            # except ValueError:
                            #     logging.error("Please enter name using numbers and characters")
            else:

                #The execute() methods run the SQL query and return the result.
                m.execute(f"select count(*) from PhoneBook where Name='{name}'")
                #This method retrieves the next row of a query result
                # set and returns a single sequence, or None if no
                # more rows are available. By default, the returned tuple
                # consists of data returned by the MySQL server,
                # converted to Python objects.
                s=m.fetchone()

                if s[0]==1:
                    logging.info("Name already exists")
                    print("Name Already Exists in Storage")
                else:


                    Mobile_no = input('Enter Mobile Number To Save:')
                    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
                    if Pattern.match(Mobile_no):
                        m.execute(f"select count(*) from PhoneBook where Mobile_no='{Mobile_no}'")
                        s = m.fetchone()

                        if s[0] ==1:
                                logging.warning("Mobile Number already exists")
                                print("Mobile Number Already exists")
                        else:

                            Field = input("Enter The Field Among(Friends or Home):")
                            if Field == 'Home' or Field == "Friends":

                                Email = input("Enter Email:")
                                regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                                if re.fullmatch(regex,Email):
                                    record=(name,Mobile_no,Field,Email)


                                    m.execute("insert into PhoneBook(Name,Mobile_no,Field,Email)values(%s,%s,%s,%s)"
                                ,record)
                                    connection.conn.commit()
                                    m.execute(f"select Name,Mobile_no from PhoneBook where Name='{name}'")
                                    s = m.fetchone()
                                    print("Name:",s[0])
                                    print("Mobile_number:",s[1])
                                    print("saved successfully")
                                    logging.info("One Data Inserted Successfully")

                                    m.close()

                                else:
                                        print("Invalid Email Id")
                            else:
                                         logging.info("\nplease choose between (Home/Friends)")
                    else:
                        print( '''\nMobile_no must fallow this rules\n1)Begins with 0 or 91\n2)Then contains 7 or 8 or 9.\n3)Then contains 9 digits\n''')

                        logging.warning('''\nMobile_no must fallow this rules\n1)Begins with 0 or 91\n2)Then contains 7 or 8 or 9.\n3)Then contains 9 digits\n''')



        except mysql.connector.Error as e:
                logging.error("Error reading data from MySQL table", e)

#user.create_record()