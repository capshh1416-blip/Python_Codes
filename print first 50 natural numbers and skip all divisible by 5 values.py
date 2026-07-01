#print first 50 natural numbers and skip all divisible 5 values.
for i in range(1,51):
    if i%5!=0:
        print(i,end=" ")
    else:
        continue