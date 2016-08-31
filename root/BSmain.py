import os
import time

#hehehe, lambda functions, me like it
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
sleep = lambda: time.sleep(0.2)


def printShit(string):
    print(string)
    clear()
    sleep()

# main function - the ever-running process
def run():
    printShit("../")
    printShit("..|")
    printShit("..\\")
    printShit("..--")
    printShit("../")
    printShit("..|")
    printShit("..\\")
    printShit("..--")


#program start exec
'''
while(True):
    run()
    '''
