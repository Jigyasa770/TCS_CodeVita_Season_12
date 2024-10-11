first, second = map(int, input().split())

if second == 0:
    print(first)
else:
    ans = first - second
    result = ans // (second + 1)
    if ans % (second + 1) != 0:
        result += 1
    print((result), end = '')
