import json
import pymysql.cursors # dunno why them and not connections...

# from pprint import pprint
from secretary.ExcelMngr import *
import json
import pymysql.cursors # dunno why them and not connections...

# from pprint import pprint
from secretary.ExcelMngr import *


# should be connected, if everyhting's right
connection = pymysql.connect(
                                 host='localhost',
                                 user='root',
                                 password='Staddy32',
                                 db='proxy',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor,
                                 autocommit=True
                             )
# the cursor which does
cur = connection.cursor()

em = ExcelManager()

print("Part1")
scanlog = []
try:
    with open('data.txt', 'r') as infile: #reading is default
        loadedDateAndList = json.load(infile)
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
            print(i,":")
            print("Hooray! ", date, studentData[3].value) #name
            insertQuery = "INSERT INTO studentvisits (StudentNumber,Date) values (" + str(studentData[3].value) + "," + str(date) + ");"
            print(insertQuery)
            cur.execute(insertQuery)