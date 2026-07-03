#Print nth Prime Number
n = int(input())
count = 0
num = 2
while True:
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    if prime:
        count += 1
        if count == n:
            print(num)
            break
    num += 1