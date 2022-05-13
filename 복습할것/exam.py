def draw_stars(n):
    if n==1:
        return '*'

n = int(input())
Stars=draw_stars(n//3)

print(draw_stars(n))
print(Stars)