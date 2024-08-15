word = "Donkey"


with open("donkey.txt","r") as f:
    content = f.read()

contentNew = content.replace("Donkey","######")

with open("donkey.txt","w") as f:
    content = f.write(contentNew)

