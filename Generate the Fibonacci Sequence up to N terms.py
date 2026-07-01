#Generate the Fibonacci Sequence up to N Terms
y=int(input())
a=0;b=1;t=0
print(a,b,end=" ")
for i in range(1,y-1):
    t=a+b
    print(t,end=" ")
    a=b;b=t