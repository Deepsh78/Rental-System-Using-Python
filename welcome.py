import calculation
import readfileOfData
import returnedd
import datetime
import billOfCustomer
#importing necessary files
def welcome_txt():
    print("""
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

                |         WELCOME TO THE SYSTEM         |
                         
                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


            Please choose one of the alternatives(1,2 or 3):
             - Renting the iems
             - Returning rented items
             - Exit
                """)#this is the welcome message
welcome_txt()
    
symbol=[]#creating lists to store symbol number and days
day=[]
def choose():
    company=readfileOfData.readFacts()
    while True:
        try:
            alternative=int(input("Enter an alternative: "))#asking for an alternative
            if alternative<1 or alternative>3:#exception case
                print("""
                ***************************************************************

                                ENTER A VALID ALTERNATIVE
                                
                ***************************************************************
                """)
            else:
                readfileOfData.printing_rows()#calling printing rows from read file of data file
                if(alternative==1):
                    print("====================================================================================")
                    while True:
                        sym_num=int(input("Enter a symbol number to update: "))
                        if (sym_num>5 or sym_num<1):
                            print("""
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                YOUR SYMBOL NUMBER IS INVALID!!!!
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            """)
                            
                        else:
                            break
                    while True:
                        number=int(input("Enter the quantity: "))
                        if (number<1):
                                print("""
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                YOUR NUMBER IS INVALID!!!!
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            """)
                        else:
                            break
                    while True:
                        days=int(input("Enter the number of days: "))
                        if (days<1):
                            print("""
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            YOUR DAYS IS INVALID!!!!
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        """)
                        else:
                            break
                    print("====================================================================================")
                                #calling function from calculation file
                    calculation.updateInfo(sym_num,company,number)
                    calculation.display(company)
                    print("""
                        -------THANK YOU FOR RENTING ITEM-------
                          """)
                    calculation.looping_fn(company,sym_num)
                                #appending user input days and symbol number in the list
                    symbol.append(sym_num)
                    day.append(days)
                elif(alternative==2):
                    print("====================================================================================")
                    while True:
                        sym_num=int(input("Enter a symbol number to return : "))
                        if (sym_num>5 or sym_num<1):
                            print("""
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                                YOUR SYMBOL NUMBER IS INVALID!!!!
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            """)
                        
                        else:
                            break
                    while True:
                        number=int(input("Enter the quantity: "))
                        if (number<1):
                             print("""
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            YOUR NUMBER IS INVALID!!!!
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        """)
                        else:
                            break
                    while True:
                        days=int(input("Enter the number of days: "))
                        if (days<1):
                            print("""
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                            YOUR DAYS IS INVALID!!!!
                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                        """)
                        else:
                            break
                            print("====================================================================================")
                            """
                                    *calling functions from returned file 

                            """
                    returnedd.updateInfoReturn(sym_num,company,number)
                    returnedd.display(company)
                    print("""
                        -------THANK YOU FOR RETURNING THE ITEM-------
                          """)
                    calculation.looping_fn(company,sym_num)
                                #appending user input days and symbol number in the list
                    symbol.append(sym_num)
                    day.append(days)
                elif(alternative==3):
                        print("""
                -------THANK YOU. PLEASE VISIT US AGAIN-------
                        """)
                        break
                else:
                        print("""
                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        
                            PLEASE ENTER A VALID ALTERNATIVE!!

                        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                        """)#in case of non valid input
        except ValueError:
                print("""===============================================

                                ENTER A VALID INPUT

                =========================================================
                """)
choose()
symbol.extend(calculation.symbol)#merging the values of both lists of this file and calculation named file 
day.extend(calculation.day)
def bill_details(symbol, day):
    while True:
        try:
            customer_bill_type = input("Enter 'B/b' for your bill: ")
            if customer_bill_type.lower() != 'b':
                print("\n~~~~~~~~~~~~~~~~~~ PLEASE ENTER A VALID LETTER ~~~~~~~~~~~~~~~~~~\n")
            else:    
                d = readfileOfData.readFacts()
                customer_selections = []
                total = 0
                for i in range(len(symbol)):
                    try:
                        penalty = 0
                        price = int(d[symbol[i] - 1][3].replace("$", ""))#replacing $ from price
                        if day[i] > 5:
                            extra_days = day[i] - 5
                            penalty = extra_days * 3
                        total += (price / 5) * day[i] + penalty
                        selections = [symbol[i], d[symbol[i] - 1][0], d[symbol[i] - 1][1], d[symbol[i] - 1][3], day[i]]
                        customer_selections.append(selections)
                    except IndexError:
                        print("================= Invalid symbol index ===============")
                customer_name, customer_number, present, unique_date = billOfCustomer.bills(customer_bill_type, total)
                bill_print(customer_name, customer_number, total, present, unique_date, customer_selections)
                return customer_name, customer_number, total, present, unique_date, customer_selections
        except ValueError:
            print("\n===============================================\n"
                  "        ENTER A VALID INPUT\n"
                  "================================================\n")
            return None, None, None, None, None, None

def bill_print(customer_name, customer_number, total, present, unique_date, customer_selections):
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("{}".format(present))
    print("                                                                            ")
    print("                                Name: {}".format(customer_name))
    print("                          Phone Number: {}".format(customer_number))
    print("                          Your grand total is: {}".format(total))
    print("                                                                             ")
    print("                                                                 {}".format(unique_date))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("{:<3}|{:<34}|{:<9}|{:<20}|".format("SN", "Item Name", "Price", "Number of selection"))
    for m in customer_selections:
        print("{:<3}|{:<34}|{:<9}|{:<20}|".format(m[0], m[2], m[3], m[4]))
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




def new_bill(customer_name, customer_number, total, present, unique_date, customer_selections):
    name_of_file = "N_" + customer_name + "_" + unique_date + "_bill.txt"
    matter = ""
    matter += "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\n" \
              "             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    matter += "\n{}\n".format(present)
    matter += "                                                                            "
    matter += " Name: {}\n".format(customer_name)
    matter += "                                                                Phone Number: {}\n".format(customer_number)
    matter += "                                                            Your grand total is: {}\n".format(total)
    matter += "                                                                             "
    matter += "                                                                 {}\n".format(unique_date)
    matter += "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\n" \
              "             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    matter += "{:<3}|{:<34}|{:<9}|{:<20}|\n".format("SN", "Item Name", "Price", "Number of selection")
    for m in customer_selections:
        matter += "{:<3}|{:<34}|{:<9}|{:<20}|\n".format(m[0], m[2], m[3], m[4])
    matter += "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`\n" \
              "             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n"
    with open(name_of_file, "w") as file:
        file.write(matter)
"""
use of with closes file itself
"""

while True:
    try:
        customer_name, customer_number, total, present, unique_date, customer_selections = bill_details(symbol, day)
        if customer_name is not None:
            new_bill(customer_name, customer_number, total, present, unique_date, customer_selections)
            break
    except ValueError:
        print("\n===============================================\n"
              "        ENTER A VALID INPUT\n"
              "================================================\n")
