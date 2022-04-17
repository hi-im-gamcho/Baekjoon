T = int(input())    # test case

k = int(input())
n = int(input())

floor = []
ho = []

for i in range(1, n+1):
    ho.append(i)

floor.append(ho)
ho = []         # 호 초기화

for x in range(1, k+1):
    for i in range(1, n+1):
        ho.append(sum(floor[x-1][0:i+1]))

    floor.append(ho)
# [
#     [1,2,3,4,5,6],
#     [],
#     [],
#     []
# ]