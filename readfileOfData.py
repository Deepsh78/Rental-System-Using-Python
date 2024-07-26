def readFacts():
    file=open("fileOfData.txt","r")#used to read file
    lines=file.readlines()
    info=[]
    for s in lines:
        s=s.replace("\n","")#removes \n
        s=s.split(",")#divides values individually "value1","value2"
        info.append(s)
    return info

def printing_rows():
    datas=readFacts()
    print("====================================================================================")
    print("{:<3}|{:<34}|{:<17}|{:<9}|{:<7}|".format("SN" , "Item Name" , "Brand" , "Price" , " Number"))#arranging labels for data
    print("""
====================================================================================
    """)
    for d in datas:
        print("{:<3}|{:<34}|{:<17}|{:<9}|{:<7}|".format(d[0],d[1],d[2],d[3],d[4]))#arranges data attractively
