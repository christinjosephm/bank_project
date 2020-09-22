class Account:
    numOfAccount = 0
    lastAccountNumber = 0

    def __init__(self, firstName, lastName, balance):
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance
        Account.numOfAccount += 1
        Account.lastAccountNumber = +1
        self.accountNumber = Account.lastAccountNumber

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if (amount < self.balance):
            self.balance -= amount
        else:
            print("Not sufficient balance to withdraw!!")

    def __str__(self):
        return f'Account Number: {self.accountNumber} \nFirst Name: {self.firstName} \nLast Name: {self.lastName} \nBalance: {self.balance}'

    def setLastAccountNumber(self, number):
        Account.lastAccountNumber = number

    def getLastAccountNumber(self):
        return Account.lastAccountNumber


# CLASS BANK
class Bank:
    '''
    CLASS BANK
    For all the account managements and storing in file, 'Bank.txt'
    '''
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