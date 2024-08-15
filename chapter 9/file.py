f = open("file.txt ","r") # we want to open the file (file.txt) in read mode
data = f.read() # read all the data of file and put it in variable data
print(data)
f.close() # closing of the file