#Compare two list same or not
ip1 = [2,3,1]
ip2 = [1,2,3]
n=len(ip1);m=len(ip2)
if sorted(ip2)==sorted(ip1):
    print('yes')
else:
    print('no')