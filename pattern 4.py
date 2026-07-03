
#4pattern 11111
#            2222
#           333
#           44
#           5
ip = int(input())
for i in range(1,ip+1):
    for j in range(ip,i-1,-1):
        print(i, end="")
    print()