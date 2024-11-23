n=int(input())
count = 0

for i in range(1,n+1):
    for j in range(1,n):
        for k in range(1,n):
            if i<j<k:
                if (i+j+k) == n:
                    count +=1
print(count)