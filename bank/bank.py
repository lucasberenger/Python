class Bank:
    bank_name = "Itau"
    user_name = "uknown" 
    deposit_receipt_counter = 0
    withdraw_receipt_counter = 0
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.balance = 1000
        print("-----------------------")
        print("Welcome", self.user_name)
        print("-----------------------")

    
    def start(self):
        print("------- Menu ----------")
        print("--- 1.check balance ---")
        print("--- 2.deposit ---------")
        print("--- 3.withdraw --------")
        print("--- 4.exit ------------")

        try:
            select = int(input("choose an option: "))
            if select == 1:
                self.check_balance()
            elif select == 2:
                self.deposit()
            elif select == 3:
                self.withdraw()
            elif select == 4:
                self.exit()
            else: 
                raise ValueError("Invalid Option")
        except ValueError as InvalidOption:
            print(f"Error: {InvalidOption}. Please, select a valid option.")
            self.start()
           
        
    def check_balance(self):
        print(f"Balance: R${self.balance}")
        self.start()
    
    def deposit(self):
        while True:
            self.deposit_receipt_counter += 1
            deposit_value = input("How much do you wish to deposit?")

            try:
                self.balance = self.balance + int(deposit_value)
            except ValueError as e:
                print(f"{e}: Only numbers are allowed.")
                continue  

            confirm = input(f"Please, confirm your deposite: \n value:{deposit_value} \n Yes(y) or No(n)?")

            try:
                if confirm == "y":
                    print("Success!")
                    print("Printing deposit receipt...")
                    with open(f'deposit_receipt_{self.deposit_receipt_counter}.txt', 'w') as file:
                        file.write(f"deposit value: R${deposit_value}\nupdated balance: R${self.balance} ")
                    with open(f'deposit_receipt_{self.deposit_receipt_counter}.txt', 'r') as file:
                        print(file.read())
                    self.start()
                    return
                elif confirm == "n":
                    continue
                else:
                    raise ValueError("Invalid Option")
            except ValueError as e:
                print(f"Error: {e}. Please, select a valid option.")
                continue
    
    def withdraw(self):
        while True:
            self.withdraw_receipt_counter += 1
            withdraw_value = input("How much do you wish to withdraw?")
            
            try:
                self.balance = self.balance - int(withdraw_value)
            except ValueError as e:
                print(f"{e}: Only numbers are allowed.")
                continue  
            
            confirm = input(f"Please, confirm your withdraw:\n value:{withdraw_value} \n Yes(y) or No(n)?")
            
            try:
                if confirm == "y":
                    print("Success!")
                    print("Printing withdraw receipt...")
                    with open(f'withdraw_receipt_{self.withdraw_receipt_counter}.txt', 'w') as file:
                        file.write(f"withdraw value: R${withdraw_value}\nupdated balance: R${self.balance}")
                    with open(f'withdraw_receipt_{self.withdraw_receipt_counter}.txt', 'r') as file:
                        print(file.read())
                        self.start()
                        return
                elif confirm == "n": 
                    continue
                else:
                    raise ValueError("Invalid Option")
            except ValueError as e:
                print(f"Error: {e}. Please, select a valid option.")
                continue
    
    
    def exit(self):
        return True
            
   
login = Bank("username")


while True:
    login.start()
    
    if login.exit():
        print("The aplication has been finished.")
        break
