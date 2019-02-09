# Jada Houser - B: 3/19/2018
# Program Set 2 - Balefron Code

from ArSeqComp import chNM, chOP
from DictionarB import noNumB, alPhaB, numAlphA, noNum

#Program 4 - Expression Tree & Stack Functions

#Includes Expression Tree class declaration and respective functions
#Needed for operations

class sequentialExpression:
    def __init__(self, dictTerm, uOper, uNumb):
        self.term = dictTerm
        self.op = uOper
        self.num = uNumb
        self.curVal = None
        self.nextOP = None
        
    def opOver(self, headList, term):
        for T in headList:
            if chOP(T) and chNM(T+1):
                opOver(T, T+1)
            
        
    def opOver(self, term, num):
        self.term = term
        self.num = num
        if self.op == '+':
            self.curVal = self.term + self.num
            self.opOver(self.curVal)
        if self.op == '-':
            self.curVal = self.term = self.num
            self.opOver(self.curVal)
        if self.op == '*':
            self.curVal = self.term * self.num
            self.opOver(self.curVal)
        if self.op == '/':
            self.curVal = self.term / self.num
            self.opOver(self.curVal)
            
            
            
            