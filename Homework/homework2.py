class Bank:
    bank_name = " ABA Bank"
    total_account = 0 

    def __init__(self , name , account):
        self.name = name
        Bank.total_account += 1
        self.account = account




    def show_owner(self):
        print(f"Owner Name: {self.name}")



    @classmethod
    def show_total_account(cls):
        print(f"Total accounts: {cls.total_account}")



    @staticmethod

    def is_valid_name(name):
        return isinstance(name , str) and len(name.strip()) >= 3

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name
        print(f"New name: {cls.bank_name} ")

    @staticmethod
    def is_valid_account_id(account_id):
        return isinstance(account_id, str) and len(account_id.strip()) == 6

student1 = Bank("Seavik", "123456")
student2 = Bank("Hello", "654321")
student3 = Bank("Dara", "111222")

student1.total_account = 100

Bank.show_total_account()

print(Bank.is_valid_name("Seavik"))