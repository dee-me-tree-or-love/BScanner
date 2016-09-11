import json
import pymysql.cursors # dunno why them and not connections...
import time
from dateutil import parser
# from pprint import pprint
from .ExcelMngr import *


# should be connected, if everyhting's right
connection = pymysql.connect(
                                 host='localhost',
                                 user='root',
                                 password='Staddy32',
                                 db='proxy',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True # so that the connection commits the transactions automatically after
                             )
# the cursor which does
cur = connection.cursor()

em = ExcelManager()

# predefined variables for the student attributes from the excel sheet
sNumberInd = 3
sNameInd = 5

print("Part1")
scanlog = []
try:
    with open('data.txt', 'r') as infile: #reading is default
        loadedDateAndList = json.load(infile)
        try:
            dtobj = parser.parse(loadedDateAndList[0])
            date = dtobj.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as excep:
            print(excep," - oups!")
            date = loadedDateAndList[0] # date of the event
        scanlog = loadedDateAndList[1] # visitors
        print(scanlog)
except:
    pass
print("Part2")
VisitorList = set(scanlog)
print(VisitorList)

'''
For each entry in the 'VISITOR LIST'
we check if its a valid number (less then 3010000 and larger then 2090000 {found using the the python script in test.py of TestBits}, cause the largest student number is 3002284)
-> we check if such student number exists
    -> we input him to the database (date and the visitor number)
'''
i = 0
for potentialVisitor in VisitorList:
    if (potentialVisitor < 3010000) and (potentialVisitor > 2090000):
        studentData = em.getStudentInfo(potentialVisitor)
        if studentData: #kinda if not null
            i = i+1
            print(i,":", studentData[sNameInd].value)
            print("Hooray! ", date, studentData[sNumberInd].value) #name
            insertQuery = "INSERT INTO studentvisits (StudentNumber, Name,Date) values (" \
                          + str(studentData[sNumberInd].value) + ",'" \
                          + str(studentData[sNameInd].value) + "','" \
                          + date \
                          + "');"
            print(insertQuery)
            try:
                cur.execute(insertQuery)
            except Exception as excep:
                print(excep)