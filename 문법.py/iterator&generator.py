# 이터러블, 이터레이터, 제너레이터에 대한 기본적인 이해가 부족...
# 이터러블과 이터레이터, 제너레이터의 차이가 뭔지 잘 모르겠음. 인터넷 찾아봐도 모르게써...



# 반복문의 기본 구문인 'for 반복자 in 반복할 수 있는 것' 에서
# '반복할 수 있는 것' == 이터러블 이다.
# 즉, 이터러블은 '내부에 있는 요소들을 차례차례 꺼낼 수 있는 객체'를 의미한다.
# ex) 리스트, 딕셔너리, 튜플 등


# 이터레이터 : 반복문의 매개변수로 전달할 수 있으며, next() 함수로 내부 요소를 하나하나 꺼낼 수 있다.



# <<제너레이터>>

def test():
    print("함수가 호출되었습니다.") 
    yield "test"

print("a 지점 통과")    
test()                  # 함수를 호출해도 함수 내부의 코드가 실행되지 않음

print("b 지점 통과")
test()                  # 함수를 호출해도 함수 내부의 코드가 실행되지 않음
print(test())           # <generator object test at 0x0000028424EC9AF0> : 제너레이터 객체

# - 함수 내부에 yield 키워드를 사용하면 해당 함수는 제너레이터 함수가 되며, 함수를 호출해도 함수 내부의 코드가 실행되지 않는다.
# - 제너레이터 함수는 제너레이터를 리턴한다.
# - 제너레이터 객체는 next() 함수의 리턴값으로 yield 키워드 뒤에 입력한 값이 출력됨. (yield 옆이 아니라 다음줄이라는 뜻인듯?)
# - next 함수를 호출한 이후 yield함수를 만나지 못하고 함수가 끝나면 'StopIteration'이라는 예외가 발생한다.

def another():
    print("a 지점 통과")
    yield 1
    print("b 지점 통과")
    yield 2
    print("c 지점 통과")
    
output = another()

print("d 지점 통과")
a = next(output)
print(a)

print("e 지점 통과")
b = next(output)
print(b)

print("f 지점 통과")
c = next(output)
print(c)

next(output)