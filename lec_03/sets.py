s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

print("After create s = set([1,2,3,4]) ")
print(s)
s.remove(2)
print("After s.remove(s)")
print(s)

print(f"The set has {len(s)} elements")
