d = {} # empty dictionary
marks = {
    "Shivansh" : 100,
    "Shubham" : 56,
    "Rohan" : 32,
    0 : "Vijay"
}

print(marks.items()) # Gives list of key value pair in tuple
print(marks.keys()) 
print(marks.values())

marks.update({"Shivansh" : 99,"Renuka" : 100}) # Dictionary are mutable
print(marks)
print(marks.get("Shivansh")) # gives value of specific key 
print(marks["Shivansh"]) # They are not same

## If specific key is not present

print(marks.get("Shivika")) # returns none
# print(marks["Shivika"]) # returns Error

value = marks.pop("Shivansh")
print(value) # returns its key value
print(marks) # print dictionary by removing particular key

item = marks.popitem()
print(item)
print(marks)

print(len(marks))


