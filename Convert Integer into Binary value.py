#Convert Integer into Binary value
n=int(input())
b,d=0,1
while n>0:
    r=n%2;
    b=b+(r*d)
    d*=10
    n//=2
print(b)