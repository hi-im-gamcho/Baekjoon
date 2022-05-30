import sys
n = int(input())
humans = [list(sys.stdin.readline().split()) for i in range(n)]

for i in range(n):
    humans[i][0] = int(humans[i][0])

humans.sort(key = lambda humans: humans[0])

for i in range(n):
    print("%d %s" %(int(humans[i][0]), humans[i][1]))

#--------------위는 내가 작성한 코드, 아래는 최종본.------------------------
#--------------내가 작성한것이 속도는 살짝 빠르지만 메모리는 더 많이 차지함(52636kb, 336ms vs 46492kb, 336ms)

people = []

for i in range(n):
    data = sys.stdin.readline().rstrip()    # 여기서 입력된 값은 모두 str형.        
    age = int(data.split()[0])              # age는 int형이고,         
    name = data.split()[1]                  # name은 str형이기 때문에
    people.append([age, name])              # 따로 저장해준다음에 합침.

people.sort(key= lambda people: people[0])

for i in range(n):
    print("%d %s" %(people[i][0], people[i][1]))




