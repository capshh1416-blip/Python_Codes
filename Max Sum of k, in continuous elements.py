# Max Sum of k, in continuous elements
n=list(map(int,input().split()))
k=int(input())
m=sum(n[:k])
c=m
for i in range(k,len(n)):
    c=c+n[i]-n[i-k]
    m=max(m,c)
print(m)