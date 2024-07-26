import readfileOfData
def updateInfoReturn(sym_num,company,number):
    try:
        number=int(number)
        sym_num=int(sym_num)
        company[sym_num-1][-1]=str(int(company[sym_num-1][-1])+number)
        symbol.append(sym_num)
        return company
        return company
    except IndexError:
        print("===========Enter a valid Number===========")
    except ValueError:
        print("===========Enter a valid Number==============")

def display(company):
    print("{:<3}|{:<34}|{:<17}|{:<9}|{:<7}|".format("SN" , "Item Name" , "Brand" , "Price" , " Number"))#formatting the label for data
    print("====================================================================================")
    for row in company:
        print("{:<3}|{:<34}|{:<17}|{:<9}|{:<7}|".format(row[0],row[1],row[2],row[3],row[4]))#arrangement of rows and column
    new_file=open('fileOfData.txt','w')#writing data in the file
    for row in company:
        new_row=",".join(row)
        new_file.write(new_row+'\n')
    new_file.close()
symbol=[]#initializing list
def returnedd_message():    
    try:
        print("====================================================================================")
        update=int(input("Enter a symbol number of the item: "))
        number=int(input("Enter the quantity: "))
        display(updateInfoReturn(update,readfileOfData.readFacts(),number))
    except ValueError:
        print("============Enter a valid Number==============")
    except IndexError:
        print("===========Enter a valid Number===============")
        

