s = {1,5,32,54,5,5,5} 

print(s,type(s))

s.add(56)
print(s,type(s))

s.remove(56)
print(s)

s.pop() # removes random element in set
print(s)


s1 = {1,4,2,5}
s2 = {5,4,3,8,0}

print(s1.union(s2))
print(s2.intersection(s1))