#Return a single digit of sum of number
s=int(input())
while s>9:
    d=0;    
    while s>0:
        d+= (s%10)
        s//=10
    s=d
print(s)