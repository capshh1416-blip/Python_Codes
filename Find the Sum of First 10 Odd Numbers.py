#Find the Sum of First 10 Odd Numbers
s=0
for i in range(1,21):
    if i%2!=0:
        s+=i
    else:
        continue
print(s)