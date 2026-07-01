#Find Largest digit from the number
n=int(input())
l=0
while n>0:
    if l<(n%10):
        l=n%10
    n//=10
print(l)