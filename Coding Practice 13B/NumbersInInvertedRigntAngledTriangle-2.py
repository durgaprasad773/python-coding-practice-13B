n=int(input())
num=0
for i in range(1,n+1):
    num = num + i


for i in range(n):
    row=""
    space="  " * i
    for j in range(n-i):
        row = row + str(num) +" "
        num = num - 1
    print(space + row)
    