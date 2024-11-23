n=int(input())
for i in range(1,n+1):
    each_row=""
    for j in range(1,i+1):
        each_row = each_row + str(j) +" "
    for k in range(1,i):
        each_row = each_row + str(k)+" "
    print(each_row)