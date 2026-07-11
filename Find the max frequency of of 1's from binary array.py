#Find the max frequency of 1's from binary array
i=list(map(int,input().split()))
c=0;m=[]
for j in i:
    if j==1:
        c+=1
    else:
        c=0
    m.append(c)
print(max(m))