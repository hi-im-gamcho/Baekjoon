n = int(input())
students = []

for i in range (n):
    x, y = map(int, input().split())
    students.append((x, y))

for a in students:
    grade = 1

    for b in students:
        if a[0] < b[0] and a[1] < b[1]:
            grade += 1
        print(grade, end=' ')
    
