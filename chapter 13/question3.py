def divisible5(n):
    if(n%5 == 0):
        return True
    return False

a = [1,23,23,32,55,50,243,70.32423,45,90]

f = list(filter(divisible5,a))
print(f)