#import os
#import time
from root.ListTrcker import *
from root.FileMngr import *
import json




#hehehe, lambda functions, me like it
#clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
#sleep = lambda: time.sleep(0.2)


def printShit(string):
    print(string)
    #clear()
    #sleep()

# main function - the ever-running process
def run(lt):
    studnumber = input()

    if(studnumber == "-1"):
        print(lt.visitorList)
    if lt.addCode(int(studnumber)):
        print("Noice")
    else:
        print("Not noice")




'''
def run():
    printShit("../")
    printShit("..|")
    printShit("..\\")
    printShit("..--")
    printShit("../")
    printShit("..|")
    printShit("..\\")
    printShit("..--")
'''

#program start exec


fm = FileManager()

while(True):

    lt = ListTracker()
    run(lt)
    uniqueStudentList = sorted(lt.visitorList)
    uniqueStudentList = set(uniqueStudentList)
    print(uniqueStudentList)
    listToSave = list(uniqueStudentList)
    with open('data.txt', 'w') as outfile:
        json.dump(listToSave, outfile)


'''

for row in fm.ws.rows:
    for cell in row:
        print(cell.value)
    print(row)
'''
