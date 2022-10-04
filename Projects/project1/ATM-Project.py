balance = 0.00             #amount in balance
otherBalance = 0.00        #amount in other balance

def getBalance(): #get balance function, returns balance
    return balance

def getOtherBalance():  #function, returns otherBalance
    return otherBalance

def printBalance():     #function, prints both balances
    print ("${}".format(round(getBalance(),2)))
    print ("${}".format(round(getOtherBalance(),2)))

def deposit(money):     #function deposits money from balance
    global balance

    if money<0 or money=="":
        print ("Invalid input! Money entered should be greater than zero")
    else:
        balance += money
        print ("Money deposit successful!")

def withdraw(money):  #function, withdraws money from balance
    global balance

    if money<0 or money>balance or money=="":
        print ("Invalid input! Money enetered should be greater than zero and less than or equal to balance")
    else:
        balance -= money
        print ("Money withdrawn seccessfully!")

def transfer(money):   #function, transfers money from balance to otherBalance
    global balance
    global otherBalance


    if money<0 or money>balance or money=="":
        print ("Invalid input! Money enetered should be greater than zero and less than or equal to balance")

    else:
        otherBalance += money
        print ("Money has been transferred from balance to otherBalance")

while True:   # loops the program
    action = input("\nWould you like to;\nprint balance, print otherBalance,\nprint both balance and otherBalance,\ndeposit money into balance, withdraw money from balance,\nor transfer money from balance to otherBalance?: ")

    if action=="exit" or action=="end" or action=="break": #break conditions
        break

    elif action=="print balance" or action=="balance":
        print("${}".format(getBalance()))

    elif action=="print otherBalance" or action=="otherBalance":
        print("${}".format(getOtherBalance()))

    elif action=="print both" or action=="print both balance and otherBalance" or action=="both":
        printBalance()

    elif action=="deposit money into balance" or action=="deposit" or action=="deposit money":
        money = float(input("how much money would you like to deposit? "))
        if money == "break" or money == "exit" or money == "end": #break conditions
            break
        else:
            deposit(money)

    elif action=="withdraw money from balance" or action=="withdraw" or action=="withdraw money":
        money = float(input("how much money would you like to withdraw? "))
        if money == "break" or money == "exit" or money == "end": #break conditions
            break
        else:
            withdraw(money)

    elif action=="transfer money from balance to otherBalance" or action=="transfer money" or action=="transfer":
        money = float(input("how much money would you like transferred? "))
        if money=="break" or money=="exit" or money=="end": #break conditions
            break
        else:
            transfer(money)

    elif action=="":
        print("Invalid entry!")

    else:
        print("Invalid entry!")
