a = [int(x) for x in input().split()]

def sum_item():
    result = 0
    for i in a:
        result += i
    return result

print(sum_item())