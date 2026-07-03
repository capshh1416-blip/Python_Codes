
#3pattern *
#              **
#              ***
#             ****
#             *****
ip = int(input())
for i in range(1,ip+1):
    for j in range(1, i+1):
        print('*', end="")
    print()
