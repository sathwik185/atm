#operations
operations=(
    "1.Balance\n",
    "2.Withdraw \n",
    "3.Deposit \n"
    "4.Transfer\n"
    "5.History\n"
    "6.Logout"
)

#accounts_table
accounts={12345:'6789',12346:'3277'}



#user details
user_details={
    12345:["chaitu",1000,"chaitu@gmail.com"],
    12346:["manu",2000,"manu@gmail.com"]

}
#login function
def login(user_name:int,password:str):
    if user_name in accounts:
        if accounts[user_name]==password:
            print("Login is successful")
            return True
        else:
            print("Wrong password")
    else:
        print("user not found")
    return False



#operations functions creation

#balance function
def balance(user_name:int):
    if user_name in user_details:
        amount=user_details[user_name][1]
        print(f"current balance is : {amount}")
    else:
        print("User not found")


#withdraw function
def withdraw(user_name:int,withdraw_amount:int):
    if user_name in user_details:
        amount=user_details[user_name][1]
        if withdraw_amount <= amount:
            user_details[user_name][1]-=withdraw_amount
            print(f"Successfully withdraw your amount :{withdraw_amount}")
            print(f"Current balance is :{user_details[user_name][1]}")
        else:
            print("Insuffucient amount in account")
    else:
        print("User not found")


#deposit function
def deposit(user_name:int,deposit_amount:int):
     if user_name in user_details:
        user_details[user_name][1]+=deposit_amount
        print(f"current balance is: {user_details[user_name][1]}")
     else:
        print("User not found")

#transfer
def transfer(user_name:int,to_account:int,transfer_amount:int):
    if user_name in user_details:
        if to_account in user_details:             
            amount=user_details[user_name][1]
            if transfer_amount <= amount:
                user_details[user_name][1]-=transfer_amount
                user_details[to_account][1]+=transfer_amount
                print(f"Current balance is : {user_details[user_name][1]}")
            else:
                print(f"insufficient amount in {user_name}")
        else:
            print(f"{to_account} User not found")
    else:
        print(f"{user_name} User not found")


#mini statement function
def history(user_name:int):
    print("Development under processing......")
    pass

#logout function
def logout():
    print("user Successfully logged out")
    exit()

#main function
if __name__=='__main__':
    print("Welcome to OurBank")
    account=int(input("Please enter account number : "))
    password=input("Enter password : ")
    if login(user_name=account,password=password):
        while True:
            print(*operations)
            choice=int(input("Please select operation : "))
            if choice==1:
                balance(user_name=account)
            elif choice==2:
                amount=int(input("Please enter your Withdraw amount :"))
                withdraw(user_name=account,withdraw_amount=amount)
            elif choice==3:
                amount=int(input("Please enter your Deposit amount :"))
                deposit(user_name=account,deposit_amount=amount)
            elif choice==4:
                receiver_account=int(input("Please enter your Receiver account number :"))
                amount=int(input("Please enter your Transfer amount :"))
                transfer(user_name=account,to_account=receiver_account,transfer_amount=amount)
            elif choice==5:
                history(user_name=account)
            elif choice==6:
                logout()
            else:
                print("Please enter between 1-6")