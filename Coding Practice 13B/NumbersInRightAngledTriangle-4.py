s=int(input())
n=int(input())

for i in range(1,n+1):
    row=""
    for j in range(2*i):
        row = row + str(s) +" "
        s=s+1
    print(row)