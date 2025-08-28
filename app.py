#operations
operations = (
    "1. Balance\n",
    "2. Withdraw\n",
    "3. Deposit\n",
    "4. Transfer\n",
    "5. History\n",
    "6. Logout"
)

#account_table
accounts ={
    12345:'6789',
    12346:'6789'
            }

#user details table
user_details = {
   12345: ["manu",1000,"manu@gmail.com"],
   12346: ["chakri",2000,"chakri@gmail.com"]


}

#login function
def login (user_name:int, password:str):
   
   #checking account present in accounts table or not
    if user_name in accounts:
        if accounts[user_name] == password:
            print("succuesfully logedin to hdfc bank")
            return True
        else:
            print("check your user credintals")
    else :
       print("User not found")
    return False

#operation funtion creation 
#balance funtion creation
def balance (user_name:int):
   print("iam in balance page")
   if user_name in user_details:
        amount= user_details[user_name][1]
        print(f"current balance is {amount}")
        #user is not in users table
   else:
        print("user not found")

#withdraw function creation 
def withdraw(user_name : int, withdraw_amount :int):
   
#check user in present table   
   if user_name in user_details:
        amount= user_details[user_name][1]
        if withdraw_amount <= amount:
            user_details[user_name][1] -= withdraw_amount
            print(f"succesfully withdraw your amount{withdraw_amount}")
            print(f"current balance is {user_details[user_name][1]}")
        else:
         print("insufficient amount in your account")
#user is not in users table
   else:
        print("user not found")
 
 #deposit funtion creation
def deposit(user_name: int, deposit_amount : int):
    if user_details in user_details:
        user_details[user_details][1] += deposit_amount
        print(f"current balance is: {user_details[user_name][1]}")
    else:
        print("user not found")



#transfer function defination
def transfer (user_name: int, to_account : int, transfer_amount : int):
    if user_name in user_details:
        if to_account in user_details:
            amount= user_details[user_name][1]
            if transfer_amount <= amount:
                user_details[user_name][1] -= transfer_amount
                user_details [to_account][1] += transfer_amount
                print(f"current balance is {user_details[user_name][1]}")
            else:
                print("insufficent amount in {user_name}")
        else:
            print(f"{to_account} user not found")
    else:
        print(f"{user_name} user not found")

    
    print("im in logout page")
    pass

#mini statement funtion 
def history(user_name :int):
    print("development under processing......")
    pass

#logout function defination
def logout():
    print("user succuesfully loggd out")
    exit()
   
#main funtion
if __name__ == "__main__":
    print("welcome to hdfc bank")
    account = int(input("please enter your account number: "))
    password = input("please enter password: ")
    while login(user_name = account, password = password):
        print(*operations)
        choice = int(input("please select your operation:"))
         
        if choice == 1:
            balance(user_name = account)
        elif choice ==2:
            amount = int(input("please enter your withdraw amount: "))
            withdraw(user_name = account, withdraw_amount=amount)
        elif choice ==3:
            amount = int(input("please enter your deposit amount: "))
            deposit(user_name=account, deposit_amount=0)
        elif choice == 4:
            reciver_account = int (input("please enter your reciver number: "))
            amount = int(input("please enter your transfer amount: "))
            transfer(user_name=account, to_account=reciver_account, transfer_amount=amount)
        elif choice ==5:
            history(user_name = account)
        elif choice ==6:
            logout()
        else:
            print("please enter between 1 - 6")
