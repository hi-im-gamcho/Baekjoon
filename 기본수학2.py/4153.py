while True:
    a = list(map(int, input().split()))
    a.sort()                                    # 오름차순 정렬
    if a[2] == 0:
        break
    if (a[2])**2 == (a[1])**2 + (a[0])**2:
        print("right")
    else:
        print("wrong")



