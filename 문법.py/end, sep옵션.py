# 1. end문의 큰따음표 안에 들어가는 내용을 넣어서 이어줌(공백 포함)
# 콘솔 창에서 "다음줄에 출력된 문자를 한 문장으로 이어주는 기능"
# 출력의 마지막에 출력되는 문자열을 설정
print("today is", end =' ')
print(2022, end = ' ')
print(1, 2, end='-')
print(9)
print()

# 2. 여러개 인자 출력시 사이에 출력되는 문자열을 설정
# sep을 사용하지 않는다면 자동적으로 sep=' ' 즉 공백으로 설정됨
# https://docs.python.org/3.8/library/functions.html#print
# 2439@@.py 참고
print("today", "is", "monday", sep='--')
