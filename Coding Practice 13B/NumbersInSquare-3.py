n=int(input())
num=1
for i in range(n):
    row=""
    for j in range(1,n+1):
        row = row + str(num)+" "
        num =num+1
    print(row)