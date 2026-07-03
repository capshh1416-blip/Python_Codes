#2pattern 1
#               12
#               123
#               1234
#               12345
ip = int(input())
for i in range(1,ip+1):
    for j in range(1, i+1):
        print(j, end="")
    print()