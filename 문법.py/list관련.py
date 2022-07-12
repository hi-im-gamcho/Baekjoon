# 리스트와 관련된 새로 알게된 것들

# 1. "리스트명.index(요소)" : 리스트의 인덱스를 반환 할 수 있다.


list_n = [1,2,3]
print(list_n.index(2))


# 2. "reversed(리스트명)" : 리스트의 요소의 순서를 뒤집고 싶을 때 사용한다
# reversed함수의 결과는 제너레이터이므로 필요한 부분에만 곧바로 사용하자!!
numbers = [1,2,3,4,5]
reversed(numbers)


# 3. 확장 슬라이싱 : 리스트를 '뒤집는' 또다른 방법
# str형에도 적용 가능하다 / int형에는 x !!
for i in numbers[::-1]: # [5,4,3,2,1]
    pass

a = 'HiHello'
print(a[::-1])          # olleHiH


# 4. 리스트화 하는 과정
word = "dkssudgktpdy"       # 일 때, 아래와 같은 차이점이 있다.

word2 = list(word)      # >>> ['d', 'k', 's', 's', 'u', 'd', 'g', 'k', 't', 'p', 'd', 'y']
word3 = [word]          # >>> ['dkssudgktpdy']


# 5. 리스트에 요소 추가
# - 리스트명.append(요소)
# - 리스트명.insert(위치, 요소) -> 리스트 중간에 요소를 추가할 수 있다. 
# - 리스트명.extend(다른 리스트) -> 리스트(a) '맨 뒤에' 리스트(b)를 추가할 수 있다. append함수르 여러 번 사용하는 효과. 
a = [1,2,3]
b = [4,5,6]
a.extend(b)     # a = [1,2,3,4,5,6]


# 6. 리스트에서 요소 제거
# - del 리스트명[인덱스]                이건 문자열에 사용할 수 없움.
# - 리스트명.pop(인덱스)                이걸 제일 많이 사용!!!!
a = [1,2,3]
print(a.pop())        # 결과 : 3
print(a)                # 결과 : [1,2]
# - 리스트명.remove(제거할 요소)        만약 제거할 요소가 여러개라면 왼쪽 하나만 제거    
# - 리스트명.clear()                    리스트 내부의 모든것 제거
a = [1,2,3]
a.clear()      # a = []


# 7. enumerate()
# - '리스트'의 요소를 반복할 때, 현재 인덱스가 몇 번째인지 확인해야 하는 경우 사용.
# - iterable에 대한 이해 필요. 
list_a = ['요소1', '요소2', '요소3']

print(f"리스트에 enumerate 함수를 적용한 출력 형태 : {list(enumerate(list_a))}") 
# 결과 : [(0, '요소1'), (인덱스값, '요소2'), (2, '요소3')]

for i, value in enumerate(list_a):
    print(f'index : {i}, value : {value}')
# 결과 : index : 0, value : 요소1
#        index : 1, value : 요소2
#        index : 2, value : 요소3



# 8. 리스트 합치기
# a = [1,2,3]
# b = [4,5,6]
# print(a+b) >>> [1,2,3,4,5,6]



# 9. 리스트 생성

# -ex1) List Comprehension (리스트 내포) (https://blog.naver.com/hhyun3032/222720858076)
# -ex2) card2 = [0] * 10    ->     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# -ex3) card3 = list(map(int, input().split()))     ->      [1, 2, 3, 4, 5, 6]  



# 10 '*'의 활용
# a = [1,2,3,4,5,6]
# print(a)                  [1, 2, 3, 4, 5, 6]
# print(*a)                 1 2 3 4 5 6
# print(*a, sep=', ')       1, 2, 3, 4, 5, 6



# 11. 인덱스에서 [::-1] 과 [-1]의 차이점
# print(a[::-1])                [6,5,4,3,2,1]
# print(a[-1])                  6

# 리스트의 요소가 하나밖에 없는 경우,
# list[-1] 로 특정 요소를 지칭할 수 있다.


# 12. 문자열 ''
# 1. word = ''
# type(word) -> str

# 2. i = input()
# word += i
# type(word) -> str
# word -> i



# 13. 리스트 + while문
# ex1) a = []   # 빈 리스트
#       while a:
#           print('Hi')     ->      아무것도 출력하지 않음.

# ex2) b = [1,2,3] # 채워진 리스트                          
#       while b:
#           print('HI')     -.      HI 무한반복
# 결론:    while b 라는 조건은 b가 있다면 (= b내부에 요소가 있다면) 이라고 해석할 수 있다.



# 14. 리스트 인덱싱
# word = '안녕하세요'
# ex1) word[-1]         요         
# ex2) word[::-1]       요세하녕안
# ex3) word[1:3]        녕하            마지막꺼는 포함 안됨.
# ex4) word[2:]         하세요
# ex5) word[:4]         안녕하세
