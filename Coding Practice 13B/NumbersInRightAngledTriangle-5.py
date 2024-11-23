s=int(input())
n=int(input())
num=0 + (s-1)
for k in range(1,n+1):
    num = num +k

for i in range(1,n+1):
    row=""
    for j in range(1,i+1):
        row = row + str(num)+" "
        num=num-1
    print(row)