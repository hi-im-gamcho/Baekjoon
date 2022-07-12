# N 번째 줄까지 주어지지만 N을 없다 -> while문으로 반복 후 try-except 구문을 이용!!
# try-except : try부분에 예외가 발생할 가능성이 있는 코드를 적고, expect부분에 예외 발생 시 실행할 코드를 적음. 

while True:
    lower, upper, digit, space = 0,0,0,0
    try:
        for i in input():
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
            elif i.isdigit():
                digit += 1
            elif i.isspace():
                space += 1
        print(lower, upper, digit, space)
    except:
        break

