# Jada Houser - B: 5/24?2017
# Program Set 2 - Balefron Code

# Program 1 - Bale Code Dictionaries

# NoNum and PuNct Sequences
noNum = { "A": 8.1, "B": 7.2, "C": 10.3, "D": 9.4, 
         "E": 5.5, "F": 8.6, "G": 10.7, "H": 8.8, 
         "I": 5.9, "J": 8.10, "K": 4.11, "L": 7.12, 
         "M": 7.13, "N": 6.14, "O": 9.15, "P": 9.16, 
         "Q": 3.17, "R": 4.18, "S": 4.19, "T": 3.20,
         "U": 9.21, "V": 6.22, "W": 3.23, "X": 8.24, 
         "Y": 8.25, "Z": 4.26, " ": 0.0 }

puNct = { ".": "0.1", "?": "0.2", "!": "0.3", "-": "0.4", 
         "...": "0.5", "''": "0.7", "'": "0.8", ",": "0.9",
         ":": "1.0", ";": "2,0", "/": "3.0", "(": "4.a", 
         ")": "4.b", "{": "5.a", "}": "5.b", "<<": "6.a", 
         ">>": "6.b", "[": "7.a", "]": "7.b", "&": "8.0", 
         "*": "9.0", "#": "10.0", "_": "11.0", "+": "12.0",
         "=": "13.0", "%": "14.0", "@": "15.0", "~": "16.0",
         "`": "17.0", "$": "18.0", "<": "19.a", ">": "19.b" }

alPha = { "A": "Pitching", "B": "Cadupag", "C": "Platzfield", 
         "D": "Parthairs", "E": "Stick", "F": "Frynells", 
         "G": "Blairfield", "H": "Eighteen", "I": "Guard", 
         "J": "Fielders", "K": "Four", "L": "Balefron", 
         "M": "Redball", "N": "Ground", "O": "Nullfield", 
         "P": "Portfield", "Q": "Air", "R": "Court", "S": "Edge",
         "T": "Six", "U": "Out-Bounds", "V": "Twelve", "W": "Ten",
         "X": "Gravnoys", "Y": "Time-Out", "Z": "Inner", " ": "Cadell"}

puNctA = { ".": "Round", "?": "Warning", "!": "Two", "-": "Merritfield", 
         "...": "Half", "''": "Penalty", "'": "Three", ",": "Contact",
         ":": "Goal", ";": "Foul", "/": "Octagon", "(": "Blueball", 
         ")": "Main", "{": "Team", "}": "EAG", "<<": "MGG", 
         ">>": "Red", "[": "Blue", "]": "MAG", "&": "EGG", 
         "*": "Coach", "#": "Referee", "_": "Captain", "+": "June",
         "=": "Fourteen", "%": "House", "@": "Pitchers", "~": "Fielders",
         "`": "Guarders", "$": "Articles", "<": "WFPS", ">": "Helmet" }

numAlph = { "0" : "zero", "1" : "one", "2" : "two", "3" : "three", "4" : "four",
            "5" : "five", "6" : "six", "7" : "seven", "8" : "eight", "9" : "nine" }

def noNumB(words):
    string = words.upper()
    newStr = []
    for let in string:
        if let >= 'A' and let <= 'Z' or let == " ":
            newStr.append(str(noNum.get(let)))
        else:
            newStr.append(puNct.get(let))
    return "-".join(newStr) 
    
def alPhaB(words):
    string = words.upper()
    newStr = []
    for let in string:
        if let >= 'A' and let <= 'Z' or let == " ":
            newStr.append(alPha.get(let))
        else:
            newStr.append(puNctA.get(let))
    return " ".join(newStr)

def numAlphA(words):
    string = words
    newStr = []
    for num in string:
        if num >= '0' and num <= '9':
            newStr.append(numAlph.get(num))
        else:
            newStr.append(num)
    return "".join(newStr)
