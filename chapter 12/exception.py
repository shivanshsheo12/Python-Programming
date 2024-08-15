# If the user input is invalid than program should not through an error
# It should be visible to the user that it was an error
try:
    a = int(input("Hey, Enter a number : "))
    print(a)

except Exception as e:
    print(e)

print("Thank you")