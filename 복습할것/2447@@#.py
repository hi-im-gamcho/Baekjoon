n = int(input())

def draw_star(n):
    if n == 1:
        return '*'

    stars = draw_star(n//3)
    lists = []

    for star in stars:
        lists.append(star * 3)              # 결과 : ['***']   
    for star in stars:
        lists.append(star + (' ' * (n//3)) + star)
    for star in stars:
        lists.append(star * 3)
    
    return lists

print('\n'.join(draw_star(n)))

 