#Convert Binary into Intger value
n=int(input())
c,s=0,0
while n>0:
    if n%10!=0:
        s+=2**c
    c+=1
    n//=10
print(s)