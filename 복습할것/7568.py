n = int(input())
students = []

for i in range (n):
    x, y = map(int, input().split())
    students.append((x, y))

print(students)

