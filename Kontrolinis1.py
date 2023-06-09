class BankAccount:
    def __init__(self, account_number):

        self.account_number = account_number
        self.balance = 0

    def deposit(self, amount):

        self.balance += amount
        return "Prideta $"

    def withdraw(self, amount):

        if self.balance >= amount:
            self.balance -= amount
            return "Isimta $"
        else:
            return "nepakanka lesu."

    def get_balance(self):

        return self.balance


# Sukuriame "BankoSąskaita" klasės objektą
account = BankAccount("1234567890")

# Pridedame pinigus
print(account.deposit(1000))

# Išimame pinigus
print(account.withdraw(500))

# Patikriname sąskaitos likutį
balance = account.get_balance()
print("Saskaitos likutis:", balance)

#####################################################################
####################################################################

