#Find max value from list without using max() function
l=list(map(int,input().split()))
m=l[0]
for i in l:
    if m<i:
        m=i
    else:
        continue
print(m)