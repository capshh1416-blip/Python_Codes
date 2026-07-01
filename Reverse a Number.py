#Reverse a Number
def rev(temp,n):
        if n<10:
            return temp*10+n
        else:
            temp=temp*10+(n%10)
            return rev(temp,n//10)
n=int(input())
print(rev(0,n))