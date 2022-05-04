x, y, w ,h = map(int, input().split())

if x >=  w - x:
    min_x = w - x
else:
    min_x = x

if y >= h - y:
    min_y = h - y
else:
    min_y = y

if min_x >= min_y:
    print(min_y)
else:
    print(min_x)


#-----------------------------------

# x, y, w ,h = map(int, input().split())

# print(min(x,y ,h-y, w-x)) 로 쉽게 가능!!