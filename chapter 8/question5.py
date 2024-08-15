def starpattern(n):
    if(n == 1): print("*")
    else: 
        print("*"*n)
        return starpattern(n-1)
    

num = int(input("Enter the number : "))
starpattern(num)

