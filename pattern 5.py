#5pattern 12345
#               1234
#               123
#               12
#               1
ip = int(input())
for i in range(ip,0,-1):
    for j in range(1,i+1):
        print(j, end="")
    print()