# 1.
for i in range(1, 10+1):
    if i == 1 or i == 2:
        print(i)
# >>> 1, 2
print()

# 2.
for i in range(1, 10+1):
    if i == 1 or 2:
        print(i)
# >>> 1,2,3,4,5,6,7,8,9,10
print()

# 3.
for i in range(1, 10+1):
    if i == (1 or 2):
        print(i)
# >>> 1
print()

# 4.
for i in range(1, 10+1):
    if i == 1 and 2:
        print(i)
# >>> 1
print()

# 5. 
for i in range(1, 10+1):
    if i == (1 and 2):
        print(i)
# >>> 2