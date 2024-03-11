
class User:
    def __init__(self,username,password, initial_balance) -> None:
        self.username = username
        self.password = password
        self.balance = initial_balance
        self.transaction_history = []
        self.loan_amount = 0
        
    def deposite(self, amount):
        self.balance += amount
        self.transaction_history.append(f"deposited {amount}")
        
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f'Withdraw {amount}')
        else:
            print(f"Bankrupt: insufficient balance to withdraw {amount}")
            
    def transfer(self, recepient, amount):
        
        if self.balance >= amount:
            self.balance -= amount
            recepient.balance += amount
            self.transaction_history.append(f"transfered {amount} to {recepient.username}")
        else:
            print(f"Bankrupt: insufficient balance to transfer")
    def take_loan(self):
        if Bank.loan_enabled:
            if self.loan_amount == 0:
                loan_limit = self.balance * 2
                self.loan_amount += loan_limit
                self.balance += loan_limit
                self.transaction_history.append(f"Took a loan of {loan_limit}")
            else:
                print(f"You already have a loan pending")
        else:
            print(f"Loan feature is currently disabled")
            
    def check_balance(self):
        return self.balance
    
    def check_transaction_history(self):
        return self.transaction_history
                
            
class Bank:
    loan_enabled = True
    
    def __init__(self) -> None:
        self.accounts = []
        
        
    def create_account(self):
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        initial_balance = int(input("Enter your initial balance: "))
        account = User(username,password,initial_balance)
        self.accounts.append(account)
    
    def get_total_balance(self):
        return sum(account.balance for account in self.accounts)
    
    def get_total_loan_amount(self):
        return sum(account.loan_amount for account in self.accounts)
    
    def toggle_loan_feature(self):
        self.loan_enabled = not self.loan_enabled

dbbl = Bank()       
while True:
    
    print("1.create account\n2.Log in to account.\n3.Exit\n")
    user_input = int(input("Enter your choice: "))
    
    if user_input == 3:
        break
    elif user_input == 1:
        dbbl.create_account()
    elif user_input == 2:
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        
        IsAdmin = False
        flag = 0
        if name == 'Admin' and password == '123':
            IsAdmin = True
        if IsAdmin == False:
            for user in dbbl.accounts:
                if user.username == name and user.password == password:
                    flag = 1
                    current_user = user
                    break
            if flag:
                while True:
                    print("WELCOME TO YOUR ACCOUNT")
                    print("1.check balance\n2.withdraw\n3.deposit\n4.transfer\n5.transaction history.\n6.take loan.\n7.Exit.\n")
                    user_input = int(input("Enter your choice: "))
                    
                    if user_input == 7:
                        break
                    elif user_input == 1:
                        print(current_user.check_balance())
                    elif user_input == 2:
                        amount = int(input("Enter amount to withdraw: "))
                        current_user.withdraw(amount)
                    elif user_input == 3:
                        amount = int(input("Enter amount to deposite: "))
                        current_user.deposite(amount)
                    elif user_input == 4:
                        recepient_name = input("Enter receiver username: ")
                        recepient = next((acc for acc in dbbl.accounts if acc.username == recepient_name),None)
                        if recepient:
                            amount = int(input("Enter amount to transfer: "))
                            current_user.transfer(recepient,amount)
                        else:
                            print("No receiver found!") 
                    elif user_input == 5:
                        print(current_user.check_transaction_history())
                    elif user_input == 6:
                        current_user.take_loan()
            else:
                print("No user found! ")
                        
        else:
            while True:
                print("WELCOME ADMIN TO THE BANK")
                print("1.Total available balance\n2.Total loan amount.\n3.Toggle loan feature.\n4.Exit.\n")
                
                a = int(input("Enter your choice: "))
                
                if a == 4:
                    break
                elif a == 1:
                    print(dbbl.get_total_balance())
                elif a == 2:
                    print(dbbl.get_total_loan_amount())
                elif a == 3:
                    dbbl.toggle_loan_feature()
           


        
   
        


    
        
        