class Bank:
    bank_name = "Itau"
    user_name = "uknown" 
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.balance = 1000
    
    def start(self):
        print("welcome", self.user_name)
        print("------- Menu ----------")
        print("--- 1.check balance ---")
        print("--- 2.deposit ---------")
        print("--- 3.withdraw --------")
        print("--- 4.exit ------------")

        select = int(input("choose an option: "))

        if select == 1:
            self.check_balance()
        elif select == 2:
            self.deposit()
        elif select == 3:
            self.withdraw()
        elif select == 4:
            self.exit()
        
    def check_balance(self):
        print(self.balance)
        self.start()
    
    def deposit(self):
        deposit_value = input("How much do you wish to deposit?")
        confirm = input(f"Please, confirm your deposite: \n value:{deposit_value} \n Yes (y) or No (n)?")
        self.balance = self.balance + int(deposit_value)

        if confirm == "y":
            print("Success!")
            print("Printing deposit receipt...")
            with open('deposit_receipt.txt', 'w') as file:
                file.write(f"deposit value: {deposit_value}\n updated balance: {self.balance} ")
            with open('deposit_receipt.txt', 'r') as file:
                print(file.read())
            self.start()
        else:
            self.deposit()
    
    def withdraw(self):
        withdraw_value = input("How much do you wish to withdraw?")
        confirm = input(f"Please, confirm your withdraw:\n value:{withdraw_value} \n Yes (y) or No (n)?")
        self.balance = self.balance - int(withdraw_value)
        
        if confirm == "y":
            print("Success!")
            print("Printing withdraw receipt...")
            with open('withdraw_receipt.txt', 'w') as file:
                file.write(f"withdraw value: {withdraw_value} \n updated balance: {self.balance}")
            with open('withdraw_receipt.txt', 'r') as file:
                print(file.read())
                self.start()
        else: 
            self.withdraw()
    
    def exit(self):
        return True
            
   
login = Bank("Lucas Berenger")


while True:
    login.start()
    
    if login.exit():
        print("The aplication has been finished.")
        break
