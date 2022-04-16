# 함수 정리

# 1. ".index())" 함수
# 형태 : "리스트명.index(요소)"
# 용도 : 객체 내에서 요소가 몇 번째 인덱스(=위치)인지 확인할 수 있다.
list_n = [1,2,3]
print(list_n.index(2))

# 2. ".count()" 함수
# 형태 : "객체.count(찾고자하는 것(=a))"
# 용도 : 객체 내에서 a가 몇번 들어가있는지 확인할 수 있다.
# a는 'str' 형태여야 한다
for i in range(0, 9+1):
    print(list_mul.count(str(i)))
    
# 3. "list()" 함수
# 형태 : "list('str형태'의 것들 또는 문자열(=a))"
# 용도 : a를 '오마분시해서' 리스트로 만들어 반환
b = list("124")
print(b)
# >>> ['1,2,4']

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

# 7. "upper()", "lower()"함수
# 형태 : '문자열'.upper(또는 lower)()
# 용도 : 문자열을 대문자 또는 소문자로 바꾸기 위해 사용

# 8. "strip()", "lstrip()", "rstrip()"함수
# 형태 : 문자열.strip()
# 용도 : 기본적으로 문자열에서 양 끝의 공백 문자를 삭제한다.
# 이때 공백 문자는 줄바꿈 문자, tab문자 등 공백의 다른 형태로 인식하 수 있는 문자들도 모두 삭제한다.
# 다만, () 내부에 다른 문자(열)(=a)을 넣으면 a가 나오지 않을 때 까지 a를 삭제한다.
# lstrip, rstrip 함수는 각각 왼, 오른쪽만을 없앰.
a = ' abcba\n\t'
a.strip()               # >>> 'abcba'
# 여러번 연속 사용이 가능하다
a.strip().strip('a')

# 9. "replace()"함수
# 형태 : "a.replace('b', 'c')"     a,b,c는 모두 문자열 
# 용도 : 문자열(string) 내 원하는 문자 변경. a 내에 있는 b를 c로 바꿈
# 여러 글자 -> 한글자 / 한글자 -> 여러 글자 또는 
# 빈 문자열로 바꾸는 것(=특정 문자(열)지움)도 가능하다
# 비파괴적 함수 
a = 'abcde abcde abcde'
a.replace('a', 'z')         # >>> zbcde zbcde zbcde
a.replace('a', 'zzz')       # >>> zzzbcde zzzbcde zzzbcde
a.replace('ab', 'z')        # >>> zcde zcde zcde
# a를 지우는 효과
a.replace('a', '')          # >>> bcde bcde bcde 
# 공백을 지우는 효과
a.replace(' ', '')          # >>> abcdeabcdeabcde
# 공백을 다른 문자로 대체
a.replace(' ', 'ㅋ')        # >>> abcdeㅋabcdeㅋabcde
# 특수 케이스 : 모든 글자 사이에 z 추가                   
a.replace('', 'z')          # >>> zazbzczdze zazbzczdze zazbzczdze  


# 10. "split()" 함수
# 형태 : 객체.split()
# 용도 : 객체를 ()안에 들어있는 것을 기준으로 쪼갬.   


# 11. 'sum()'
# ()내부의 내용물을 다 더한다.


