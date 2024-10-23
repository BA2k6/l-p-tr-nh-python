x = list(map(int, input().split()))
b=1
while (x[0] + b) <= x[2]:
    if (x[0]+b)%x[1] == 0:
        print(b, end = " ")
    b += 1
if b==1:
    print("-1")