import sys
n = int(input())
result = []

for i in range(n):
    result.append(int(sys.stdin.readline()))

for x in sorted(result):
    sys.stdout.write(str(x) + '\n')

