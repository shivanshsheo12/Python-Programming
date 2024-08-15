def sum(n):
    if(n == 1):
        return 1
    else: return n + sum(n-1)

number = int(input("Enter the number : "))
print(sum(number))