# Jada Houser - B: 5/24/2017
# Program Set 2 - Balefron Code

from DictionarB import noNumB, alPhaB, numAlphA

# Program 2 - User Input and Program Output
def progMenu():
    print("                        Balefron Program 1 - Translation")
    print("==========================================================================================")
    print("1. Translate String To NoNum Sequence | 3. To File | 5. Line From File | 7. Para From File")
    print("------------------------------------------------------------------------------------------")
    print("2. Translate String To Alpha Sequence | 4. To File | 6. Line From File | 8. Para From File")
    print("==========================================================================================")

def userInp():
    progMenu()    
    seqCh = int(input("Please choose a sequence option: "))
    if seqCh == 1:
        userIn = input("Please enter a string to be translated: ")
        print(noNumB(numAlphA(userIn)))
        goAgain()
    elif seqCh == 2:
        userIn = input("Please enter a string to be translated: ")
        print(alPhaB(numAlphA(userIn)))
        goAgain()
    elif seqCh == 3:
        userNm = input("Please enter a filename and file type to write to\nExample: fileNw.txt\n")
        baleFl = open(userNm, "w")
        userIn = input("Please enter a string to be translated: ")
        baleFl.write("Your string was:\n" + userIn + "\n\n")
        baleFl.write("In the NoNum sequence:\n" + noNumB(numAlphA(userIn)))
        baleFl.close()
        print("Opening file named " + userNm + "...\n")
        baleRe = open(userNm, "r")
        print(baleRe.read() + "\n")
        baleRe.close()
        goAgain()
    elif seqCh == 4:
        userNm = input("Please enter a filename and file type to write to\nExample: fileNw.txt\n")
        baleFl = open(userNm, "w")
        userIn = input("Please enter a string to be translated: ")
        baleFl.write("Your string was:\n" + userIn + "\n\n")
        baleFl.write("In the Alpha sequence:\n" + alPhaB(numAlphA(userIn)))
        baleFl.close()
        print("Opening file named " + userNm + "...\n")
        baleRe = open(userNm, "r")
        print(baleRe.read() + "\n")
        baleRe.close()
        goAgain()
    elif seqCh == 5:
        """Note: This function will fail if the file contains parts of either sequence.
        Update this file by erasing the extraneous sequence or other text that is not 
        meant to be translated. For the example file, load it into the workspace. After 
        the first run, ignore the first suggestion to save. Press space then save it as
        it was originally. This also applies to the paragraph function (seqCh 7 & 8)."""
        userFn = input("Please enter the filename and file type to read from\nExample: fileStr.txt\n")
        baleRf = open(userFn, "r+")
        fileTx = str(baleRf.read())
        baleRf.write("\nYour string in the NoNum sequence:\n" + noNumB(numAlphA(fileTx)))
        baleRf.close()
        print("Appending to and opening file named " + userFn + "...\n")
        baleWf = open(userFn, "r")
        print(baleWf.read() + "\n")
        baleWf.close()
        goAgain()
    elif seqCh == 6:
        userFn = input("Please enter the filename and file type to read from\nExample: fileStr.txt\n")
        baleRf = open(userFn, "r+")
        fileTx = str(baleRf.read())
        baleRf.write("\nYour string in the Alpha sequence:\n" + alPhaB(numAlphA(fileTx)))
        baleRf.close()
        print("Appending to and opening file named " + userFn + "...\n")
        baleWf = open(userFn, "r")
        print(baleWf.read() + "\n")
        baleWf.close()
        goAgain()
    elif seqCh == 7:
        """Went through the file using a for loop, assigned each line to an element in a list, 
           removed the newline characters, then iterated over it with the NoNum function, writing 
           it to the file."""
        text = []
        userFn = input("Please enter the filename and file type to read from\nExample: paraStr.txt\n")
        balePfn = open(userFn, "r+")
        for line in balePfn:
            text.append(line.rstrip('\n'))
        balePfn.write("\n\nThe lines have been translated into the NoNum sequence...\n")
        for i in range(0, len(text)):
            balePfn.write("\n" + str(i + 1) + ") '" + text[i] + "':\n" + noNumB(numAlphA(text[i])) + "\n")
        balePfn.close()
        baleRf = open(userFn, "r")
        print("Appending to and opening file named " + userFn + "...\n\n")
        print(baleRf.read() + "\n")
        baleRf.close()
        goAgain()
    elif seqCh == 8:
        text = []
        userFn = input("Please enter the filename and file type to read from\nExample: paraStr.txt\n")
        balePfn = open(userFn, "r+")
        for line in balePfn:
            text.append(line.rstrip('\n'))
        balePfn.write("\n\nThe lines have been translated into the Alpha sequence...\n")
        for i in range(0, len(text)):
            balePfn.write("\n" + str(i + 1) + ") '" + text[i] + "':\n" + alPhaB(numAlphA(text[i])) + "\n")
        balePfn.close()
        baleRf = open(userFn, "r")
        print(baleRf.read() + "\n")
        baleRf.close()
        goAgain()
    else:
        print("That sequence option does not exist.")
        userInp()
    
def goAgain():
    userRep = input("Would you like to go again? Y or N ")
    if userRep == 'Y' or userRep == 'y':
        userInp()
    elif userRep == 'N' or userRep == 'n':
        print("Program ended.")
    else:
        print("Invalid input.")
        goAgain()     
    
    
userInp() 
