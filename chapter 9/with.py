f = open("file.txt")
print(f.read())
f.close()


# This same can be done using with statement
with open("file.txt") as f:
    print(f.read())

# You dont have to explicitly close the file