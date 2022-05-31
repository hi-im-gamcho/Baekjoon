# 리스트와 관련된 새로 알게된 것들

# 1. "리스트명.index(요소)" : 리스트의 인덱스를 반환 할 수 있다.
from ast import comprehension


list_n = [1,2,3]
print(list_n.index(2))


# 2. "reversed(리스트명)" : 리스트의 요소의 순서를 뒤집고 싶을 때 사용한다
# reversed함수의 결과는 제너레이터이므로 필요한 부분에만 곧바로 사용하자!!
numbers = [1,2,3,4,5]
reversed(numbers)


# 3. 확장 슬라이싱 : 리스트를 뒤집는 또다른 방법
# str에도 적용 가능하다 / int형에는 x !!
numbers[::-1]


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
# - del 리스트명[인덱스]
# - 리스트명.pop(인덱스)                이걸 제일 많이 사용!!!!
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



# 8. item()
# - '딕셔너리의' 키와 값을 조합해야할 때 사용.



# 9. List Comprehension (https://blog.naver.com/hhyun3032/222720858076)