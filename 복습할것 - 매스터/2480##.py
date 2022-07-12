
# 1번째 풀이
a, b, c = [int(x) for x in input().split()] 
if a==b==c:
    print(10000 + (a*1000))
elif a==b:
    print(1000 + (a*100))
elif b==c:
    print(1000 + (b*100))
elif c==b:
    print(1000 + (c*100))
else:
    print(max(a,b,c)*100)

# 2번째 풀이 (sort() 사용)
d,e,f = map(int, input().split())
g = [d,e,f]
g.sort()
if d==e==f: 
    price = 10000 + (d*1000)

elif d!=e and e!=f and f!=d:   # 이거를 d!=e!=f라고 적으면 안되는게 이렇게되면 1,2,1을 True로 받아들임 
    price = 100*g[2]
else:
    price = 1000 + (g[1]*100)
print(price)


