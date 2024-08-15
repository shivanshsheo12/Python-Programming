# If the user input is invalid than program should not through an error
# It should be visible to the user that it was an error
try:
    a = int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")           # This else will only be executed when I try is true.


try:
    a = int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I am inside finally")        # Finally will be executed after try and else both     