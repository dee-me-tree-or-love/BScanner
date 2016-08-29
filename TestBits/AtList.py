class AttList:

    def __init__(self):
        self.StudList = []

    def Add(self, ):

    def Check(self, inpid):
        if inpid > 0:
            first = 0
            thelist = self.StudList
            last = len(thelist) - 1
            found = False

            while first <= last and not found:
                middle = (first + last) // 2  # integer division
                if thelist[middle] == inpid:
                    found = True
                else:
                    if inpid < thelist[middle]:
                        last = middle - 1
                    else:
                        first = middle + 1
            index = middle;
            return found, index
        else:
            return False, -1;


    def Check(thelist, inpid):
        if inpid>0:
            first = 0
            last = len(thelist) - 1
            found = False

            while first <= last and not found:
                middle = (first + last) // 2 #integer division
                if thelist[middle] == inpid:
                    found = True
                else:
                    if inpid < thelist[middle]:
                        last = middle - 1
                    else:
                        first = middle + 1
            index = middle;
            return found, index
        else:
            return False, -1;