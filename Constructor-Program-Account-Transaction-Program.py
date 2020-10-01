# Program 1 :-
# First Constructor Program in Python
class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        return

    def display(self):
        print('A value is :', self.a)
        print('B value is :', self.b)
        return

    def main():
        t1 = Test(10, 20)
        t2 = Test('Python', 'Django')

        t1.display()
        t2.display()
        return


Test.main()


# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 2 :-
# Second Constructor Program in Python
class Test1:
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        return

    def withdraw(self):
        print('Available Balance is :', self.balance)
        print('Trying to withdraw amount :', self.amount)
        if self.amount <= self.balance:
            final = self.balance - self.amount
            print('Collect the Cash...!!')
            print('Final Balance is :', final)
        else:
            print('Insufficient Balance in your Account...!!')
        return

    def main():
        t = Test1(2000, 500)
        t.withdraw()
        return


Test1.main()


# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Program 3 :-
# Third Constructor Program in Python
class Account:
    def __init__(self, balance):
        self.balance = balance
        return

    def getbalance(self):
        return self.balance

    def withdraw(self, amount):
        print('Trying to Withdraw Amount :', amount)
        print('Available Blanace is :', self.balance)
        if amount <= self.balance:
            print('Please Collect Your Cash...!!')
            self.balance = self.balance - amount
        else:
            print('Insufficient Balance in your Account...!!')
        return


class Bank:
    def main():
        amount = int(input('Enter the Initial Amount :'))
        acc = Account(amount)
        print('Balance is :', acc.getbalance())
        amount = int(input('Enter the Withdraw Amount :'))
        acc.withdraw(amount)
        print('Final Balance in you Account is :', acc.getbalance())
        return


Bank.main()

# =-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
