# for only listing the stuff


import time
import json
import os
#this method sucks, since the other script is loaded and evaluated before
#from todeploy.SecMain import run


# reserved words:
extcomm = 666
secrcomm = "secr"


visitorList = []
eventdate = time.strftime("%Y-%m-%d %H:%M:%S");
# to prevent loss of data, if RPi was restarted for instance
try:
	with open('data.txt', 'r') as infile: #reading is default
		loadedDateAndList = json.load(infile)
		eventdate = loadedDateAndList[0] # date of the event
		visitorList = loadedDateAndList[1] # visitors
	print('loaded log')
except:
	print('new log')
	pass

studnumber = 0;
while(studnumber!= extcomm and studnumber!= secrcomm):
	try:
		studnumber = input()
		#print(studnumber)
	except:
		pass
	#print('so far so good')
	#unless the exit was entered
	try:
		
		studnumber = int(studnumber)
		if(studnumber >= 1500000 and studnumber <=3200000):
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
		else:
			print("not a student")
	except:
		print("nonononon")

if(studnumber == extcomm or studnumber == 0):
	print("quited")
if(studnumber == secrcomm):
	print("bye-bye, now secretary is in control")
	##run()
	# this works though
	#os.system("python SecMain.py")
