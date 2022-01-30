# this is a simple bank system I create this after learn oop concepts in python
# created by Ameer Almughalis

from datetime import datetime

class Customer:
    balance = 0
    dateTime = datetime.now()
    dateFormat = dateTime.strftime('%A, %d %B %Y, %I %M %p')

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Deposit {amount}YR to your bank balance on {self.dateFormat}')
        return self.balance

    def withdrowal(self, amount):
        self.balance = self.balance - amount
        print(f'{amount} were deducted from your bank balance on {self.dateFormat}')
        return self.balance

    def balance_query(self):
        print(f'Your current balance is {self.balance}')


ameer = Customer()
ameer.deposit(500)
ameer.balance_query()
ameer.withdrowal(150)
ameer.balance_query()