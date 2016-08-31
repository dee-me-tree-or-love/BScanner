class Mimi:
    def __int__(self,kek):
        self.kiki = "fufu"

class Complex:
    def __init__(self, realpart):
        self.r = realpart
        self.i = 7

#Binary search throught the list
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
#Whatevs list
alist = [0,1,3,4,7,8,99]

#Shit to look for
item = 0
while item != 'bullshit':
    try:
        item = int(input())
    except:
        item = -1;

    x = Complex(3)
    print(x.i)

    x = Mimi(3)
    print(x.Kiki)

    #Analysing
    res,index = Check(alist,item)
    print(index, res)

    if (not res) & (index >0):
        afrontsliceoflist = alist[:index]
        alastsliceoflist = alist[index:]
        #afrontsliceoflist.append(item)
        print(alist," kek ",afrontsliceoflist)
        print("take that: ", afrontsliceoflist, " + ", alastsliceoflist)
        alist = afrontsliceoflist
        print
        alist = alist + alastsliceoflist
        print(alist, "TADA!")
    else:
        print("Already there")