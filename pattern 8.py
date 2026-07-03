#8pattern 54321
#            5432
#           543
#           54
#           5

ip = int(input())
for i in range(ip,0,-1):
    for j in range(ip, ip-i,-1):
        print(j, end="")
    print()