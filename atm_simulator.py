class Atm:
    def __init__(self):
        self.money = 0
    
    def invest_money(self):
        try:
            add_money = int(input("Please enter the amount of money you want to invest\n"))
            self.money += add_money
        except ValueError:
            print("Please enter a valid number.")
    
    def withdraw_money(self):
        try:
            withdraw_money = int(input("Please enter the amount of money you want to withdraw\n"))
            if withdraw_money > self.money:
                print("Insufficient balance!")
            else:
                self.money -= withdraw_money
        except ValueError:
            print("Please enter a valid number.")
    
    def show_money(self):
        print(f"Current balance: {self.money}")

money = Atm()

while True:
    choose_operation = input("1-Invest Money\n2-Withdraw Money\n3-Show Money\n4-Quit\n")
    if choose_operation == "1":
        money.invest_money()
    elif choose_operation == "2":
        money.withdraw_money()
    elif choose_operation == "3":
        money.show_money()
    elif choose_operation == "4":
        print("Quitted!")
        break
    else:
        print("Please enter a valid option!")
