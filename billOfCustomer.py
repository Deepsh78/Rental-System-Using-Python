import datetime # module to access the date and time
def bills(customer_bill_type,total):
    present=datetime.datetime.now()#this is the object for current date and time
    unique_date=present.strftime("%y%m%d%H%M%S")#formats date and time into string
    customer_name=""
    customer_number=""
    while True:
        customer_name=input("Dear Customer! Enter your name: ")
        if not customer_name.isnumeric():
            break
        else:
             print("""
    ###########################################################

          THE NAME SHOULD NOT CONTAIN NUMERIC VALUES!!!!!
            
    #############################################################
            """)
    while True:
        customer_number=input("Enter your phone number too: ")
        if customer_number.isnumeric():
            break
        else:
             print("""
###########################################################

              ENTER VALID PHONE NUMBER!!!!!
        
#############################################################
        """)
        
    return customer_name,customer_number,present,unique_date#returns mentioned values

    
