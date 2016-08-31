# for only listing the stuff

# import os
# import time
import json

visitorList = []

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
