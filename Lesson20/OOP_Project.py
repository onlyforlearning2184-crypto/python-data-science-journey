# from Bank_acc import *
import Bank_acc as ba

tirth = ba.bank_acc(1000, "Tirth")
rachit = ba.bank_acc(3000, "Rachit")

tirth.get_balance()
rachit.get_balance()

tirth.deposit(1000)

rachit.withdraw(1500)
rachit.deposit(1000)

tirth.withdraw(3000)
tirth.withdraw(300)

tirth.transfer(20000, rachit)
tirth.deposit(1000)
tirth.deposit(1000)

krupa = ba.Interest_Reward_Act("krupa", 2000)

krupa.get_balance()

raviraj = ba.Savings_Acc("Raviraj", 50000)

raviraj.get_balance()
raviraj.deposit(3000)
raviraj.withdraw(5000)
raviraj.deposit(6000)
