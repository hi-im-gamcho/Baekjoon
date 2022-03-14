h, m = map(int, input().split())
# h (0 ≤ h ≤ 23)
# m (0 ≤ m ≤ 59)
# timer (0 ≤ timer ≤ 1,000)
timer = int(input())

h += timer//60
m += timer%60

if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24

print(h, m)

