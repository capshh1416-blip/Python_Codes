
#7pattern 55555
#            4444
#           333
#           22
#           1
ip = int(input())
for i in range(ip,0,-1):
    for j in range(i, 0, -1):
        print(i, end="")
    print()