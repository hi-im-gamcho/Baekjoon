a, b, v = map(int, input().split())

day = (v-a)/(a-b)+1

if day == int(day):
    print(day)
else: 
    print(int(day)+1)