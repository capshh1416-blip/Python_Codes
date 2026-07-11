#Print all sub-array
n=list(map(int,input().split()))
for i in range(len(n)):
    for j in range(i,len(n)):
        print(n[i:j+i])