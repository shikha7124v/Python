# Append 
l = [11,45,2,4,6]
print(l)
l.append(19)
print(l)

# Sort
print(l.sort())
print(l.sort(reverse=True))
print(l.reverse)

# Index
print(l.index(45))

# Count
print(l.count(2))

# Reference of l to m
m = l
m[0] = 0
print(l)

# Copy of l to m
m = l.copy()
m[0] = 0
print(l)

# Insert at index
# l.index(1, 100)
print(l)

# extend
m = [900, 1000, 1100]
l.extend(m)
print(l)

# Concatenate
k = l+m
print(k)
