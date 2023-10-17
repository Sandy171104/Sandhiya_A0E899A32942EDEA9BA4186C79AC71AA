
class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__account_balance = initial_balance

    def deposit(self, amount):
        self.__account_balance += amount

    def withdraw(self, amount):
        if amount <= self.__account_balance:
            self.__account_balance -= amount
        else:
            print("Insufficient funds.")

    def display_balance(self):
        return self.__account_balance

# Create an instance of the BankAccount class
account = BankAccount("1234567890", "John Doe", 1000)

# Test deposit functionality
account.deposit(500)

# Test withdrawal functionality
account.withdraw(200)

# Test display balance functionality
balance = account.display_balance()
print("Account Balance:", balance)