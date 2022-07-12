N = int(input())
circles = list(map(int, input().split()))

def gcd(x,y):
    while y != 0:
        x,y = y, x%y
    return x

for circle in circles[1:]:
    min = gcd(circles[0], circle)
    print(f'{circles[0] // min}/{circle // min}')