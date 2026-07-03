#10pattern *****
#           ****
#            ***
#             **
#              *
n=int(input())
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="  ")
    for l in range(n,i-1,-1):
        print("*",end=" ")
    print()