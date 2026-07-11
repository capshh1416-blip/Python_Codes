#Write a function next_greater_element(arr) that
#takes a list of integers and returns a list where each
#element is replaced by the next greater element to its
#right in the array. If no such element exists, use -1
i= list(map(int,input().split()))
m=[]
for j in range(len(i)):
    x=-1
    for k in range(j+1,len(i)):
        if i[k]>i[j]:
            x=i[k]
            break
    m.append(x)
print(m)