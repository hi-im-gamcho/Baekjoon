input_num = int(input())
line_num = 0
max_num = 0

while input_num > max_num:
    line_num += 1               # line_num 이 하나씩 증가할 때 마다
    max_num += line_num         # max_num - min_num 도 하나씩 증가. 

gap = max_num - input_num

if line_num % 2 == 0:
    top = line_num - gap
    bot = gap + 1
else:
    top = gap + 1
    bot = line_num - gap

 
# 1 / 2 / 3 / 4 

 
