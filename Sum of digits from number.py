#Sum of digits from number
i=int(input())
s=0
while i>0:
    s+=i%10
    i=i//10
print(s)