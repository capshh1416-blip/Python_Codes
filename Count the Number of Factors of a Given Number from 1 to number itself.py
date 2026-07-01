#Count the Number of Factors of a Given Number from 1 to number itself
n=int(input())
f=2
for i in range (2,n//2+1):
    if n%i==0:
        f+=1
print(f)