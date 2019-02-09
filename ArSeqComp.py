# Jada Houser - B: 5/25/2017
# Program Set 2 - Balefron Code

# Program 3 - Ar.Seq. Composition
# Example input: *123/12+3

#This contains the functions needed to take in the ArSeq, no pushing
#Or popping from the stack variable lyAr

def readMen():
    print("Hi! You're currently in the Ar.Seq. Composition program, where you can write out an Ar.Seq of your own")
    print("and see it applied to the original No.Num sequence. To accomplish this, we'll have you enter your Ar.Seq.")
    print("one operation and number at a time until you decide what number to end on.")

lyAR = []

def fOP():
    userOp = input("Please enter the first operation: ")
    if chOP(userOp) == 0:
        print("Invalid input")
        fOP()
    else:
        lyAR.append(userOp)
        uAR()

def uAR():
    userIn = input("Please enter a number: ")
    if chNM(userIn) == 0:
        print("Invalid input")
        uAR()
    elif chNM(userIn) == 1:
        lyAR.append(userIn)
        uOP()
    else:
        lyAR.append(chNM(userIn))
        uOP()
    
def uOP():
    userQu = input("Would you like to continue and enter an operation? Y or N ")
    if userQu == 'y' or userQu == 'Y':
        userIn = input("Please enter an operation: ")
        if chOP(userIn) == 0:
            print("Invalid input")
            uOP()
        else:
            lyAR.append(userIn)
            uAR()
    elif userQu == 'n' or userQu == 'N':
        uARseq = str("".join(lyAR))
        print("This is your Ar.Seq.: " + uARseq)
        print(lyAR)
        #return/place lyAR into the stack function here
    else:
        print("Invalid input")
        uOP()

def chOP(usrO):
    if usrO == '*' or usrO == '/' or usrO == '-' or usrO == '+':
        return 1
    else:
        return 0

def chNM(usrN):
    i = 1
    add = 0
    if usrN[0] == '0':
        newUsN = usrN.replace("0", "")
        for i in range(1, len(newUsN)):
            if newUsN[i] >= '0' and newUsN[i] <= '9':
                add = add + 1
                i = i + 1
        if add == len(newUsN) - 1:
            return newUsN
        else:
            return 0
    elif usrN[0] >= '1' and usrN[0] <= '9':
        for i in range(1, len(usrN)):
            if usrN[i] >= '0' and usrN[i] <= '9':
                add = add + 1
                i = i + 1 
        if add == len(usrN) - 1:
            return 1
        else:
            return 0
    else:
        return 0
     
fOP()