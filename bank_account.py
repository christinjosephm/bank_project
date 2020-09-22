class Account:
    numOfAccount = 0
    lastAccountNumber = 0

    def __init__(self, first_name, last_name, balance):
        self.first_name = first_name
        self.lastName = last_name
        self.balance = balance
        Account.numOfAccount += 1
        Account.lastAccountNumber = +1
        self.accountNumber = Account.lastAccountNumber

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
        else:
            print("Not sufficient balance to withdraw!!")

    def __str__(self):
        return f'Account Number: {self.accountNumber} \nFirst Name: {self.first_name} \nLast Name:{self.last_name} \nBalance: {self.balance}'


def get_last_acc_number(self):      # STATIC Functions of Account to get the last account Number
    return Account.lastAccountNumbe


def set_last_acc_number(self, number):  # STATIC Function of Account tp set last account Number
    Account.lastAccountNumber = number


# CLASS BANK
class Bank:
    """
     CLASS BANK
    For all the account managements and storing in file, 'Bank.txt'
    """
    dictAccounts = {}

    def __init__(self):
        try:
            myfile = open('Bank.txt', 'r')
            mylist = myfile.readlines()
            for accountStr in mylist:
                accountSplit = accountStr.split()
                a = Account(accountSplit[0], accountSplit[1].accountSplit[2])
                dictAccounts[accountSplit[0]:a]
            myfile.close()

        except FileNotFoundError:
            print("No file found")
            myfile = open('Bank.txt', 'w')
            myfile.close()

    def writeToFile(self):
        mylist = []
        for acc in dictAccounts.values():
            mylist.append(f'{acc.accountNumber} {acc.firstName} {acc.lastName} {acc.balance}')
        myfile = open('Bank.txt', 'w')
        myfile.writelines(mylist)

    def openAccount(self, firstName, lastName, balance):
        acc = Account(firstName, lastName, balance)
        dictAccounts[acc.accountNumber:acc]