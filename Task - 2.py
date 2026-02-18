class BankAccount:
    """
    A class to represent a bank account with deposit and withdraw functions.
    """
    def __init__(self, owner, balance=0.0):
        """
        Initialize the account with an owner and an optional starting balance.
        """
        self.owner = owner
        self.balance = balance
        print(f"Hello {self.owner}! Account created with an initial balance of {self.balance:.2f}.")

    def deposit(self, amount):
        """
        Deposit funds into the account.
        """
        if amount > 0:
            self.balance += amount
            print(f"Amount Deposited: {amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw funds from the account, checking for sufficient balance.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"You Withdrew: {amount:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def display_balance(self):
        """
        Display the current balance of the account.
        """
        print(f"\n{self.owner}'s Current Available Balance = {self.balance:.2f}")


my_account = BankAccount("Alice", 1000.0)


my_account.display_balance()
my_account.deposit(500.0)
my_account.withdraw(200.0)
my_account.withdraw(1500.0) 
my_account.display_balance()
