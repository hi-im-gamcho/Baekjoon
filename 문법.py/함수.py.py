# 함수 정리

# 1. ".index())" 함수
# 형태 : "리스트명.index(요소)"
# 용도 : 객체 내에서 요소가 몇 번째 인덱스(=위치)인지 확인할 수 있다.
list_n = [1,2,3]
print(list_n.index(2))

# 2. ".count()" 함수
# 형태 : "객체.count(찾고자하는 것(=a))"
# 용도 : 객체 내에서 a가 몇번 들어가있는지 확인할 수 있다.
for i in range(0, 9+1):
    print(list_mul.count(str(i)))
    
# 3. "list()" 함수
# 형태 : "list('str형태'의 것들 또는 문자열(=a))"
# 용도 : a를 '오마분시해서' 리스트로 만들어 반환
b = list("124")
print(b)
# >>> ['1,2,4']

num = list(map(int, input()))
print(num)
# a = [123] 형태와의 차이점 -> 오마분시 여부

# 4. "map()" 함수
# 형태 : "map(함수, iterable)"
# 용도 : iterable 의 각 요소들을 함수처리하여 반환한다
# list화 시켜야 출력 가능 
sub_num = list(map(int, input().split()))
print(sub_num)

# 5. "ord()" 함수
# 형태 : "ord(숫자 또는 알파벳 대,소문자)"
# 용도 : 문자 또는 숫자의 아스키 코드 값을 되돌려주는 함수
print(ord(input()))

# 6. "chr()" 함수
# 형태 : "chr(아스키코드 값)"
# 용도 : 아스키코드에 해당하는 숫자를 문자열로 변환
word = input()
alphabets = list(range(97, 123))    # 알파벳의 아스키코드 범위

for alphabet in alphabets:
    print(word.find(chr(alphabet)))
    