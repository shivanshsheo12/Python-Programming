a = int(input("Enter marks of english : "))
b = int(input("Enter marks of maths : "))
c = int(input("Enter marks of science : "))

percentage = ((a + b + c)/300)*100

if( a>=33 and b>=33 and c>=33 and percentage>=40 ): print("Pass !!")
else: print("Fail !!")  