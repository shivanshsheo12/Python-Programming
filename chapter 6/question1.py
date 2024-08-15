a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))
d = int(input("Enter the fourth number : "))

max = a
if(max<b): max = b
if(max<c): max = c
if(max<d): max = d

print("maximum number is ",max)

if(a>b): max1 = a
else: max1 = b

if(c>d): max2 = c
else: max2 = d

if(max1>max2): max3 = max1
else: max3 = max2

print(max3)


