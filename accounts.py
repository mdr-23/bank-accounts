""" BANK ACCOUNTS SIMULATOR (CUSTOMERS INFO) """


class Account:
    def __init__(self, user_id, name, address, balance=0):
        self.user_id = user_id
        self.name = name
        self.address = address
        self.balance = balance

    def get_balance(self):
        return self.balance

    #deposites function
    def deposite(self, ammount):
        self.balance = self.balance + ammount
        return self.balance

    #withdraws function
    def withdraw(self, ammount):
        if ammount < self.balance:
            self.balance -= ammount
            return self.balance
        else:
            print("Funds are not enought")

#CUSTOMER 1
customer1 = Account("10", "Harry Kane", "Hurricane 10")
customer1.deposite(150000)
customer1.withdraw(35000)
print(customer1.__dict__)
print("Su saldo es: £", customer1.balance)

#CUSTOMER 2
customer2 = Account("11", "Gareth Bale", "Wales 11")
customer2.deposite(300000)
customer2.withdraw(80000)
print(customer2.__dict__)
print("Su saldo es: £", customer2.balance)

#CUSTOMER 3
customer3 = Account("7", "Heung Min Son", "Sonny Street 7")
customer3.deposite(100000)
customer3.withdraw(15000)
print(customer3.__dict__)
print("Su saldo es: £", customer3.balance)

#CUSTOMER 4
customer4 = Account("33", "Ben Davies", "Wales 33")
customer4.deposite(40000)
customer4.withdraw(75000)
print(customer4.__dict__)
print(customer4.get_balance())