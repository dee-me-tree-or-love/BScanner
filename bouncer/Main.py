# for only listing the stuff


import time
import json

visitorList = []
date = time.strftime("%d/%m/%Y");
# to prevent loss of data, if RPi was restarted for instance
try:
    with open('data.txt', 'r') as infile: #reading is default
        loadedDateAndList = json.load(infile)
        date = loadedDateAndList[0] # date of the event
        visitorList = loadedDateAndList[1] # visitors
except:
    pass

while(True):

    studnumber = input()

    try:
        studnumber = int(studnumber)
        visitorList.append(studnumber)
        '''
        uniqueStudentList = sorted(prog.visitorList)
        uniqueStudentList = set(uniqueStudentList)
        print(uniqueStudentList)
        '''
        listToSave = visitorList
        with open('data.txt', 'w') as outfile:
            json.dump(listToSave, outfile)
        print("noice")
    except:
        print("nonononon")
