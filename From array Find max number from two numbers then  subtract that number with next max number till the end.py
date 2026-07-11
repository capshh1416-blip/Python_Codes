#From array Find max number from two numbers then 
#subtract that number with next max number till the end.
n=list(map(int,input().split()))
m=max(n[0],n[1])
c=m
for i in range(1,len(n)):
    if n[-1]==n[i+1]:
        c=abs(c-max(n[i],n[-1]))
        break
    else:
        c=abs(c-max(n[i],n[i+1]))
print(c)