class BankAccount:
    """
    A class representing a bank account with basic banking operations.
    
    Attributes:
        account_balance (float): The current balance in the account
    """
    
    def __init__(self, initial_balance=0):
        """
        Initialize a BankAccount with an optional starting balance.
        
        Args:
            initial_balance (float): The starting balance for the account.
                                    Defaults to 0 if not specified.
        """
        self.account_balance = initial_balance
    
    def deposit(self, amount):
        """
        Add funds to the account.
        
        Args:
            amount (float): The amount to deposit into the account
        """
        self.account_balance += amount
    
    def withdraw(self, amount):
        """
        Withdraw funds from the account if sufficient balance exists.
        
        Args:
            amount (float): The amount to withdraw from the account
            
        Returns:
            bool: True if withdrawal was successful, False if insufficient funds
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
