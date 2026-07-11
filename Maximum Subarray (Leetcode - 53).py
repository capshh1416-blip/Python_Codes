# Maximum Subarray (Leetcode - 53)
n=list(map(int,input().split()))
m=[]
for i in range(len(n)):
    for j in range(i,len(n)):
        m.append(abs(sum(n[i:j+1])))
print(max(m))