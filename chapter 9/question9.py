with open("copy.txt") as f:
    content = f.read()

with open("paste.txt","w") as f:
    f.write(content)
