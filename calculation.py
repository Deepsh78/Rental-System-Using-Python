import readfileOfData
import returnedd
"""
importing necessary files
"""
def updateInfo(sym_num,company,number):
    try:
        number=int(number)
        sym_num=int(sym_num)
        company[sym_num-1][-1]=str(int(company[sym_num-1][-1])-number)#accessing the quantity and subtracting it
        return company
    except IndexError:
        print("===========Enter a valid Number===========")#handling error
    except ValueError:
        print("===========Enter a valid Number==============")

def display(company):
    print("{:<3}|{:<34}|{:<30}|{:<9}|{:<7}|".format("SN" , "Item Name" , "Brand" , "Price" , " Number"))
    print("====================================================================================")
    for row in company:
        print("{:<3}|{:<34}|{:<30}|{:<9}|{:<7}|".format(row[0],row[1],row[2],row[3],row[4]))#arranging rows and column properly
    new_file=open('fileOfData.txt','w')
    for row in company:
        new_row=",".join(row)
        new_file.write(new_row+'\n')#writing the data in file
    new_file.close()

def calculation_again(update,number):
    try:
        print("====================================================================================")
        update=int(input("Enter a symbol number of the item: "))
        number=int(input("Enter the quantity: "))
        display(updateInfo(update,readfileOfData.readFacts(),number))
    except ValueError:
        print("============Enter a valid Number==============")
    except IndexError:
        print("===========Enter a valid Number===============")
    

symbol=[]
day=[]
customer_selections=[]
def looping_fn(company,sym_num):
    company = readfileOfData.readFacts()
    print("====================================================================================")
    while True:
        try:
            ask_again=str(input("Do you want to rent,return or quit? "))
            if ask_again.lower()=="quit":
                break
            elif ask_again.lower()=="return":
                print("====================================================================================")
                #asking user for inputs
                while True:
                    sym_num=int(input("Enter the symbol number to return: "))
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
                returnedd.updateInfoReturn(sym_num,company,number)
                print("====================================================================================")
                returnedd.display(company)#writes the new info in the file
                day.append(days)
                symbol.append(sym_num)
                customer_selections.append((sym_num, company[sym_num - 1][1], company[sym_num - 1][2], company[sym_num - 1][3], number))
            elif ask_again.lower()=="rent":
                    print("====================================================================================")
                    #asking user for inputs
                    while True:
                        sym_num=int(input("Enter a symbol number of the item: "))
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
                    updateInfo(sym_num,company,number)#updating the information
                    print("====================================================================================")
                    display(company)
                    day.append(days)
                    symbol.append(sym_num)
                    customer_selections.append((sym_num,company[sym_num - 1][1], company[sym_num - 1][2], company[sym_num - 1][3], number))


        except ValueError:
            print("============Enter a valid Number==============")#handling errors
        except IndexError:
            print("===========Enter a valid Number===============")
        
         
            

"""
1,Velvet Table Cloth,Saathi,$8,20
2,Microphone Set,Audio Technica,$189,15
3,Disco Light Set, Sonoff,$322,24
4,Surround Sound Speaker Set,Dolby,$489,4
5,Dinner Table 8x5,Panda Furnitures,$344,8
readfileOfData.readFacts()

"""
