# 함수를 사용한다 = 함수를 호출한다
# 함수를 호출할 때는 괄호 내부에 여러가지 자료를 넣게 됨
# 이러한 자료를 '매개변수'라고 부름
# 함수를 호출해서 최종적으로 나오는 결과를 '리턴값'이라고 부름
def 함수(매개변수):
   변수 = 초깃값
   여러가지 처리들
   return 변수

# 1. 리턴(return) : 함수를 실행했던 위치로 돌아가라는 뜻으로, 함수가 끝나는 위치를 의미.
# 따라서 return 키워드를 만나는 순간 함수가 종료됨
# 자료 없이 리턴하기
def return_test():
    print("위치 a")
    return 
    print("위치 b")

print(return_test)
# >>> 위치 a

# 자료와 함께 리턴하기
def return_test2():
    return 100

value = return_test2()
print(value)
# >>> 100



