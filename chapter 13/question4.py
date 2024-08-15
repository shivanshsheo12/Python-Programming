from functools import reduce
a = [1,23,23,32,55,50,243,70,45,90]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,a))