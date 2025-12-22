class Balance_Exception(Exception):
    pass


class bank_acc:
    def __init__(self, initial_ammount, acc_name):
        self.balance = initial_ammount
        self.name = acc_name
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f} ")

    def get_balance(self):
        print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.get_balance()

    def viable_Transaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise Balance_Exception(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            self.viable_Transaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.get_balance()
        except Balance_Exception as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n***************\n\nBeginning Transfer..🚀🚀")
            self.viable_Transaction(amount)
            self.get_balance()
            self.withdraw(amount)
            account.deposit(amount)
            self.get_balance()
        except Balance_Exception as error:
            print(f"\nTransfer interrupted. ❌❌ {error}")
        else:
            print("\nTransfer complete! ✔️✔️")

    # def withdraw(self, amount):
    #     if self.balance >= amount:
    #         self.balance = self.balance - amount
    #         print("\nWithdraw complete.")
    #         self.get_balance()
    #     else:
    #         print(
    #             f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
    #         )
    #         raise Balance_Exception(
    #             f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
    #         )


class Interest_Reward_Act(bank_acc):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.get_balance()


class Savings_Acc(Interest_Reward_Act):
    def __init__(self, initial_ammount, acc_name):
        super().__init__(initial_ammount, acc_name)
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.viable_Transaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.get_balance()
        except Balance_Exception as error:
            print(f"\nWithdraw interrupted: {error}")
