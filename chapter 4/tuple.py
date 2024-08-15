a = (1, 2, 5, 6)
print(type(a)) # class tuple

b = (1)
print(type(b)) # will return class int becuase python will consider that variable b is assign with int 1

c = (1,)
print(type(c)) # will return class as tuple

# a[0] = 345 # Throughs an error # because tuple are imutable

print(a)