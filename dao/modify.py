import logging
import dao.display as v
logging.basicConfig(filename='C:\\Users\\Harish Reddy\\PycharmProjects\\phonebook application\\dao\\service\\log.txt',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)


from dao.Propertyfile.dbconnection import connection
class edit:
        ''' modify method will update the user records according user needs by using
        mysql update command'''
        @staticmethod
        def modify():
                v.display.disp()
                name=input("Enter Name of the person you want to update :")

                cur=connection.conn.cursor()
                sql=f"select * from PhoneBook where Name='%{name}%'"
                cur.execute(sql)
                res=cur.fetchone()
                if res==[]:
                        print("empty")
                else:
                        print("Choose the option you want to update")
                        print("1,Name")
                        print("2,mobile_no")
                        print("3,field")
                        print("4,email")
                        ch = int(input("enter your choice:"))
                        if ch == 1:
                                n=input("Enter new name:")
                                sql=f"update PhoneBook set Name='{n}' where Name='{name}'"
                                cur.execute(sql)
                                connection.conn.commit()
                                print("Name updated Succesfully")
                        elif ch==2:
                                mob=input("Enter new Mobile Number:")
                                sql = f"update PhoneBook set Mobile_no='{mob}' where Name='{name}'"
                                cur.execute(sql)
                                connection.conn.commit()
                                logging.info("Mobile_no updated Succesfully")
                                print("Mobile_no updated Succesfully")
                        elif ch == 3:
                                fld=input("Enter new field ")
                                sql=f"update PhoneBook set Name='{fld}' where Name='{name}'"
                                cur.execute(sql)
                                connection.conn.commit()
                                print("Field updated Succesfully")
                        elif ch == 4:
                                eid=input("Enter new email ")
                                sql=f"update PhoneBook set Name='{eid}' where Name='{name}'"
                                cur.execute(sql)
                                connection.conn.commit()
                                print("Email updated Succesfully")
                        else:
                                print("invalid choice")
#edit.modify()




