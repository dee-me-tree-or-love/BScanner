# for only listing the stuff


import time
import json
import os
#this method sucks, since the other script is loaded and evaluated before
#from todeploy.SecMain import run


# reserved words:
extcomm = "exit"
secrcomm = "secr"


visitorList = []
eventdate = time.strftime("%Y-%m-%d %H:%M:%S");
# to prevent loss of data, if RPi was restarted for instance
try:
    with open('data.txt', 'r') as infile: #reading is default
        loadedDateAndList = json.load(infile)
        eventdate = loadedDateAndList[0] # date of the event
        visitorList = loadedDateAndList[1] # visitors
except:
    pass

while(True):

    studnumber = input()
    #unless the exit was entered
    if(studnumber!=extcomm and studnumber!=secrcomm):

        try:
            studnumber = int(studnumber)
            visitorList.append(studnumber)
            '''
            uniqueStudentList = sorted(prog.visitorList)
            uniqueStudentList = set(uniqueStudentList)
            print(uniqueStudentList)
            '''
            listToSave = [eventdate,visitorList]
            with open('data.txt', 'w') as outfile:
                json.dump(listToSave, outfile)
            print("noice")
        except:
            print("nonononon")
    else:
        #calls the method of the secreatary
        break
if(studnumber == extcomm):
    print("quited")
if(studnumber == secrcomm):
    print("bye-bye, now secretary is in control")
    ##run()
    # this works though
    os.system("python SecMain.py")