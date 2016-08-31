from root import FileManager

# used to keep track of students entering the event
class ListTracker:

    fm = 0
    visitorList = []

    # initialized with an empty list of visitors
    def __int__(self):
        self.visitorList = [0,1,2,3]
        self.fm = FileManager()

    # finds if a number already exists in the list
    # returns the RESULT OF A SEARCH [TRUE/FALSE]
    # and an INDEX [integer] where it has TO BE LOCATED, if NOT found
    def findCodeBinary(self, studnumber):
        # since student numbers are well... numbers
        if (studnumber > 0) and (self.visitorList):
            first = 0
            last = len(self.visitorList) - 1
            found = False

            while first <= last and not found:
                middle = (first + last) // 2  # integer division

                if self.visitorList[middle] == studnumber:
                    found = True #good, now return
                    return found, middle #yes, found -yes, there
                else:
                    if studnumber < self.visitorList[middle]:
                        last = middle - 1
                    else:
                        first = middle + 1
            # apparently had not found anything, but stopped with the index of a closest smaller element
            index = middle;
            #found == false, index = newindex-1
            return found, index
        # some motherfucker tried to input a not valid integer
        else:
            return False, -1

    # verifies whether the new entry should be placed at the end and adds it if so
    # returns the result in boolean: true, if added, false - if was not supposed to
    def checkAddingToLastEntry(self, studnumber):
        newsbigger = studnumber > self.visitorList[
                                                    len(self.visitorList)-1
                                                    ]
        if newsbigger:
            self.visitorList.append(studnumber) #added, if was true, so no need to continue
        return newsbigger


    # to try adding the code to the list
    def addCode(self,studnumber):


        if self.fm.testStudentNumber(studnumber): # if this student number exists
                # now it will try to add it
            if not (self.checkAddingToLastEntry(studnumber)): #if it is larger than the last - it can never be found before the last, since the list is sorted ascending
                # if adding was not succesful
                res,index = self.findCodeBinary(studnumber)
                print (res,index)

        '''
        afrontsliceoflist = self.visitorList[:index]
        alastsliceoflist = self.visitorList[index::]
        afrontsliceoflist.append(studnumber)
        #print(self.visitorList, " only a part of it's here now ", afrontsliceoflist)
        self.visitorList = afrontsliceoflist
        self.visitorList = self.visitorList + alastsliceoflist
        #by now the visitorList is modified and has a
        '''

''' check method, probably not needed
    # checks if the code is valid to be added
    def checkCode(self,studNumber):
'''
# testing purposes
lt = ListTracker()
res,index = lt.findCodeBinary(2758599)
print(res,index)
