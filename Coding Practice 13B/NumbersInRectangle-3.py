m=int(input())
n=int(input())
k=n*m
for i in range(m):
    row=""
    for j in range(n):
        row = row + str(k) +" "
        k=k-1
    print(row)