from functools import reduce


# def square(n):
#     return n*n

# Shortcut for creating simple functions
square = lambda x:x*x

print(square(5))


# Convert the whole list in one string by joining it through some Signal
a = ["Shivansh","Gaurav","Shreyash","Anish"]
final = "::".join(a)
print(final)

# Formating
a = "{1} is a good {0}".format("Shivansh","boy")

print(a)


# Mapping
l = [1,2,3,4,5]

square = lambda x: x*x

sqList = map(square,l)
print(list(sqList))

# Filter Example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even,l)
print(list(onlyEven))

# Reduce Example
def sum(a,b):
    return a + b

print(reduce(sum,l))