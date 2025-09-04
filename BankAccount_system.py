class Bank_Account_System:
    def __init__(self, username, account_number):
        self.username = username
        self.account_number = account_number
<<<<<<< HEAD
        self.balance = 500.0
=======
        self.balance = 0.0
>>>>>>> origin/main
 
    def deposit(self, amount):
        self.balance += amount
        return f"Deposited {amount}. New balance: {self.balance}"
 
    def show_balance(self):
        return f"Current Balance: {self.balance}"
 
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        else:
            self.balance -= amount
<<<<<<< HEAD
            return f"Withdraw {amount}. New balance: {self.balance}"
=======
            return f"Withdrew {amount}. New balance: {self.balance}"
>>>>>>> origin/main
 
    def account_details(self):
        return (f"Account Holder: {self.username}\n"
                f"Account Number: {self.account_number}\n"
                f"{self.show_balance()}")
 
class SavingsAccount(Bank_Account_System):
    def __init__(self, username, account_number, interest_rate):
        super().__init__(username, account_number)
        self.interest_rate = interest_rate
 
    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest
        return f"Interest applied. New balance: {self.balance}"
 
class CurrentAccount(Bank_Account_System):
    def __init__(self, username, account_number, overdraft_limit):
        super().__init__(username, account_number)
        self.overdraft_limit = overdraft_limit
 
    def withdraw(self, amount):
        if amount > (self.balance + self.overdraft_limit):
            return "Overdraft_Limit exceeded"
        else:
            self.balance -= amount
            return f"Withdrew {amount}. New balance: {self.balance}"
 
if __name__ == "__main__":
    username = input("Enter account holder name: ")
    account_number = input("Enter account number: ")
 
    account1 = Bank_Account_System(username, account_number)
    print(account1.account_details())
<<<<<<< HEAD
    print(account1.deposit(20000))
    print(account1.withdraw(3000))
=======
    print(account1.deposit(10000))
    print(account1.withdraw(1500))
>>>>>>> origin/main
    print(account1.show_balance())
 
    savings_username = input("Enter savings account holder name: ")
    savings_account_number = input("Enter savings account number: ")
<<<<<<< HEAD
    savings = SavingsAccount(savings_username, savings_account_number, 3)
    print(savings.account_details())
    print(savings.deposit(10000))
=======
    savings = SavingsAccount(savings_username, savings_account_number, 6)
    print(savings.account_details())
    print(savings.deposit(5000))
>>>>>>> origin/main
    print(savings.apply_interest())
    print(savings.show_balance())
 
    current_username = input("Enter current account holder name: ")
    current_account_number = input("Enter current account number: ")
<<<<<<< HEAD
    current = CurrentAccount(current_username, current_account_number, 300)
    print(current.account_details())
    print(current.deposit(2000))
=======
    current = CurrentAccount(current_username, current_account_number, 200)
    print(current.account_details())
    print(current.deposit(1000))
>>>>>>> origin/main
    print(current.withdraw(1100)) 
    print(current.show_balance())
    print(current.withdraw(300)) 
    print(current.show_balance())