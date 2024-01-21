def calc(num, item):
    if item == '@': return num*3
    elif item == '%': return num+5
    elif item == '#': return num-7

n = int(input())

for _ in range(0, n):
    a = list(input().split(" "))
    num = float(a.pop(0))

    for i in a:
        num = calc(num, i)
        
    print("%.2f" % num)