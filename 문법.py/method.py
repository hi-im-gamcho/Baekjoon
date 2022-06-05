# 함수 정리

# 1. ".index())" 함수
# 형태 : 리스트명.index(요소)
# 용도 : 객체 내에서 요소가 몇 번째 인덱스(=위치)인지 확인할 수 있다.
list_n = [1,2,3]
print(list_n.index(2))




# 2. ".count()" 함수
# 형태 : 객체.count(찾고자하는 것(=a))
# 용도 : 객체 내에서 a가 몇번 들어가있는지 확인할 수 있다.
# a는 'str' 형태여야 한다
for i in range(0, 9+1):
    print(list_mul.count(str(i)))
    



# 3. "list()" 함수
# 형태 : list('str형태'의 것들 또는 문자열(=a))
# 용도 : a를 '오마분시해서' 리스트로 만들어 반환
b = list("124")
print(b)
# >>> ['1,2,4']




# 4. "map()" 함수
# 형태 : map(함수, iterable)
# 용도 : iterable 의 '각 요소들을' '함수처리하여' 반환한다.
# list화 시켜야 출력 가능 
# -ex1)
sub_num = list(map(int, input().split()))
print(sub_num)

# -ex2)
n, m = map(int, input().split())    #1) 1 13  #2) 1 2 3
print(n)    # 1     #2)에러 발생
print(m)    # 13



# 5. "ord()" 함수
# 형태 : ord(숫자 또는 알파벳 대,소문자)
# 용도 : 문자 또는 숫자의 아스키 코드 값을 되돌려주는 함수
print(ord(input()))




# 6. "chr()" 함수
# 형태 : chr(아스키코드 값)
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
# 기능 : 객체를 ()안에 들어있는 것을 기준으로 쪼갬.
# 비파괴적 함수이다.

# ex1) 'how are you?'.split() => ['how', 'are', 'you?']  

# split() vs split(' ')
# split(' ')은 공백을 하나 없애주고, 나머지 공백은 각각을 하나의 요소로 만들어준다.
# split()은 공백이 몇 칸이든 상관없어 전부 없애준다.




# 11. 'sum()'
# ()내부의 내용물을 다 더한다.
# -ex) sum(10, 30, 50) -> 90 




# 12. "zfill()"
# 형태 : '문자열'.zfill(전체 문자열의 길이)
# 기능 : 문자열 앞에 원하는 만큼 0으로 채움.
# 전체 문자열의 길이가 문자열의 길이와 같거나 그 이상일 때는 0이 출력되지 않는다.



# 13. "reverse()" 와 '문자열 슬라이싱[::-1]'
# 형태 : 'reverse(객체 또는 문자열)
# 기능 : 문자열 또는 객체 내부의 것을 역순으로 만든다.
# 파괴적 함수.

# '문자열 슬라이싱[::-1]' : 역순을 의미
# - ex) map(int, input()[::-1].split())




# 14. "abs()"
# 형태 : abs(숫자)
# 기능 : 절댓값을 반환한다.
# - ex) print(abs(-1, -10))




# 15. 'min()', 'max()'
# 형태 : min(숫자들 또는 객체)
# 기능 : 최소, 최댓값 반환.




# 16. 'join()'
# 형태 : '구분자'.join(리스트)
# 기능 : 매개변수로 들어온 리스트에 내부의 요소 하나하나를 합쳐서 하나의 '문자열로 바꾸어 반환'.
#        이때 구분자는 리스트의 요소 사이에 들어가 요소들을 구분하는 역할을 한다.
# 비파괴적 함수이다.
#        
# -ex1) join(['a', 'b', 'c'])    =>      'abc'      =>      구분자가 없는 경우.
# -ex2) '*'.join(['a', 'b', 'c'])   =>   'a*b*c
# -ex3) ' '.join(['a', 'b', 'c'])    => 'a b c'      =>     구분자가 공백인 경우.




# 17. 'capitalize()' vs 'title()' vs 'swapcase()'
# 형태 : 문자열.capitalize() / 문자열.title() / 문자열.swapcase()
# 기능 : 문자열의 첫 글자만을 대문자로 만든다. / 각 단어들의 첫 글자만을 대문자로 만든다. / 대문자와 소문자를 바꾼다.
# -ex) a = 'how aRe you?'
# -ex1) print(a.capitalize())   =>  How are you?
# -ex2) print(a.title())        =>  How Are You?
# -ex2) print(a.swapcase())     =>  HOW ArE YOU?




# 18. 'startwith()' vs 'endwith()'
# 형태 : 객체.startwith(a) / 객체.endwith(a)
# 기능 : 객체가 a로 시작하는지 / 끝나는지 확인하고싶을 때 사용.
# -ex) print('가천대학교'.startwith('가천')) => True




# 19. 'filter()'
# 형태 : filter(함수, 리스트)
# 기능 : 리스트의 요소를 함수에 넣고, 리턴값이 True인 것으로 새로운 리스트를 구성해주는 함수.
# -ex) new_list = filter(function, old_list)




# 20 '&'
# 형태 : 'a&b' (a,b는 숫자, 문자열 또는 집합)
# 기능 : a,b의 교집합을 return한다.
