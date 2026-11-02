
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, new_owner):
        if not isinstance(new_owner, str):
            raise TypeError("Owner name must be a string.")

        if len(new_owner.strip()) < 3:
            raise ValueError("Owner name must be at least 3 characters.")

        self.__owner = new_owner.strip()

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        if isinstance(new_balance, bool) or not isinstance(new_balance, (int, float)):
            raise TypeError("Balance must be a number.")

        if new_balance < 0:
            raise ValueError("Balance cannot be negative.")

        self.__balance = new_balance


account = BankAccount("Seavik", 1000)

print("Owner:", account.owner)
print("Balance:", account.balance)

account.owner = "Dara"
account.balance = 2000

print("Updated Owner:", account.owner)
print("Updated Balance:", account.balance)
