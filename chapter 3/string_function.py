name = "Shivansh"

print(len(name)) # gives the length of the function
print(name.endswith("nsh")) # gives boolean value
print(name.startswith("Shiv")) # gives boolean value
print(name.capitalize()) # Capitalize the starting word
print(name.find("v")) # Finds the index
print(name.replace("Shivansh","Mahesh")) # Can replace any character/set of character/even Whole string


## Escape sequence character

a = "Shivansh is a god boy\nbut not a bad boy" #\n but the post string after \n in new line
print(a)

b = "Shivansh is a god \"boy\" "
print(b)

c = "Shivansh is good boy\tbut not a bad boy"
print(c)