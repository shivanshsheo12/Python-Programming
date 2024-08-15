import math


class Calculator:
    def __init__(self,n):
        self.square = n*n
        self.cube = n*n*n
        self.squareroot = math.sqrt(n)
    def getoutput(self):
        print(f"Square : {self.square}")
        print(f"Cube : {self.cube}")
        print(f"Square Root : {self.squareroot}")

n = int(input("Enter the input : "))
number = Calculator(n)
number.getoutput()