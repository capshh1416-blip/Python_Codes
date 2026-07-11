#print numbers from given input with adding zeros in front
m,n=map(int,input().split())
s=""
L=[]
w=""
for i in range(m,n+1):
    s=str(i)
    w=""
    if i <10:
        w=w+'00'+s
        L.append(w)
    elif i<100 and i>=10:
        w=w+'0'+s
        L.append(w)
    elif i>=100 and i<=999:
        w=w+s
        L.append(w)
for j in L:
   print(j ,end=" ")