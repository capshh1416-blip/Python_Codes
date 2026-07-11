#4) add every 2 value from list 
# ip: 3 4 1 6 7 8 
#op: 7 5 7 13 15
l=list(map(int,input().split()))
for i in range(len(l)-1):
    print(l[i]+l[1+i],end=" ")