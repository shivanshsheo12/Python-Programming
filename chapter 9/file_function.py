f  = open("file.txt")

# line = f.readlines() # this comes in as a list

# print(line,type(line))

line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
line4 = f.readline()
print(line1,type(line1))
print(line2,type(line2))
print(line3,type(line3))
print(line4,type(line4))

f.close()