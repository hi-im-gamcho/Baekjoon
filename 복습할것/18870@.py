import sys

n = int(sys.stdin.readline().rstrip())
num_list = list(map(int, sys.stdin.readline().split()))
dic = {y:x for x,y in enumerate(sorted(set(num_list)))}

for x in num_list:
    print(dic[x], end=' ')

