class ATM:
    def __init__(self):
        self.balance = 0
    
    def check_balance(self):
        return f"Your balance is {self.balance}"
    
    def deposit(self, amount):
        self.balance += amount
        return f"{amount} deposited. Your new balance is {self.balance}"
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return f"{amount} withdrawn. Your new balance is {self.balance}"
        else:
            return "Insufficient funds"
    
def main():
    atm = ATM()
    
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            print(atm.check_balance())
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: "))
            print(atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            print(atm.withdraw(amount))
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
