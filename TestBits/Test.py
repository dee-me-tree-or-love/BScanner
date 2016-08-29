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




    #Analysing
    res,index = Check(alist,item)
    print(index, res)

    if (not res) & (index >0):
        afrontsliceoflist = alist[:index]
        alastsliceoflist = alist[index::]
        afrontsliceoflist.append(item)
        print(alist," kek ",afrontsliceoflist)
        alist = afrontsliceoflist
        alist = alist + alastsliceoflist
        print(alist, "TADA!")
    else:
        print("Already there")