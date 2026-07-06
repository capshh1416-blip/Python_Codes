#Average of array elements
l=list(map(int,input().split()))
c,s=0,0
for i in l:
    c+=1
    s+=i
print(s//c)