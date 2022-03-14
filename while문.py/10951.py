while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    # 입력이 아무것도 없으면 종료
    except:
        break
