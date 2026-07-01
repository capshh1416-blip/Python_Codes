# ATM 
def checkbal():
    if bal==0:
        print("Acc Empty")
    else:
        print(bal)
def withdraw (amt,bal):
        print("amt taken: ",amt)
        return (abs(bal-amt))
def deposite(amt,bal):
    return (amt+bal)	
Pass=int(input())
bal=1000
if Pass==123:
    print("Welcome")
    print("1. Show balance\n2.Withdraw\n3.Deposite\n4.Exit")
    while True:
        x=int(input("Enter your choice (1/2/3/4): "))
        match x:
            case 1:
                checkbal()
            case 2:
                w=int(input("enter amt: "))
                if bal<w:
                    print("insufficient ")
                elif w%100!=0:
                    print("Enter valid amt")
                else:
                    bal=withdraw(w,bal)
                    print("amt withdrawl completed")
            case 3:
                d=int(input("enter amt: "))
                bal=deposite(d,bal)
                print("amt deposited: ",d)
                print("amt deposit completed")
            case 4:
                print("thank you")
                break;
            case _:
                print("invalid")
        print()
