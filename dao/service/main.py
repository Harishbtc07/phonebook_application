import logging

import dao.userrecords as u
import dao.search as s
import dao.modify as m
import dao.findjunk as f
import dao.display as v
import dao.delete as d

logging.basicConfig(filename='C:\\Users\\Harish Reddy\\PycharmProjects\\phonebook application\\dao\\service\\log.txt',
                            filemode='a',
                            format='%(asctime)s, %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)
'''we used Logging, is a Python module in the standard library 
that provides the facility to work with the framework for 
releasing log messages from the Python programs. Logging is used 
to tracking events that occur when the software runs.'''
# in this module we are calling every operation that we performed on the PhoneBookApp


#Creating and Configuring Logger


#Testing our Logger

def menu():

    while True:
        print("------Main Menu-------")
        print("1.Add Record")
        print("2.Search Record")
        print("3.Modify Record")
        print("4.FindJunk Record")
        print("5.Display Record")
        print("6 Delete Record")
        try:
            ch=int(input("Select Your Option (1-6):"))

            if ch==1:
                print("Add new Records")
                u.user.create_record()
            elif ch==2:
                print("Searching new records")
                c=int(input("Choose 1 for Search by name or choose 2 for search by Number:"))

                if c == 1:
                    s.search.searchByname()
                elif c == 2:
                    s.search.searchByNumber()
            elif ch == 3:
                print("Modify records")
                m.edit.modify()
            elif ch == 4:
                print("Finding unused numbers")
                f.findjunk.find()
            elif ch == 5:
                print("Displaying Records")
                v.display.disp()

            elif ch==6:
                print("Deleting a user")
                d.delete.remove()
            else:
                print("Invalid choice")
        except ValueError:
            print("Please Enter The digits")




'''If the python interpreter is running that module (the source file) as the 
main program, it sets the special __name__ 
variable to have a value “__main__”. If this file is being imported from 
another module, __name__ will be set to the module’s name. Module’s name is 
available as value to __name__ global variable. 
A module is a file containing Python definitions and statements. 
The file name is the module name with the suffix .py appended. '''
if __name__ == "__main__":

    print("\n***************PhoneBooK Application**************")
    logging.info("Execution starts from here")
    menu()