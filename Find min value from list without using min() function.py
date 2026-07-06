#Find min value from list without using min() function
l=list(map(int,input().split()))
mi=l[0]
for i in l:
    if mi>i:
        mi=i
    else:
        continue
print(mi)