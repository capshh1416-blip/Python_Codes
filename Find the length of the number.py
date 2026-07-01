# Find the length of the number
i=int(input())
c=0
while i>0:
    c+=1
    i//=10
print(c)