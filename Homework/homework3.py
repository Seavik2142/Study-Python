from abc import ABC, abstractmethod


# ---------------------------------------------------------
# 1. Custom Exceptions
# ---------------------------------------------------------
class InsufficientFundsError(Exception):
  """Raised when the account does not have enough funds."""

  pass


class InvalidTransactionError(Exception):
  """Raised when a transaction is invalid."""

  pass


# ---------------------------------------------------------
# 2. Abstract Base Class
# ---------------------------------------------------------
class Account(ABC):

  def __init__(self, account_number: str, owner: str, balance: float = 0.0):
    self.__account_number = account_number
    self._owner = owner
    self._balance = balance
    self._transactions = []

  @property
  def account_number(self):
    return self.__account_number

  @property
  def balance(self):
    return self._balance

  @abstractmethod
  def deposit(self, amount: float):
    pass

  @abstractmethod
  def withdraw(self, amount: float):
    pass

  @abstractmethod
  def calculate_interest(self):
    pass

  def __str__(self):
    return f"[{self.__class__.__name__}] ID: {self.__account_number} | Owner: {self._owner} | Balance: ${self._balance:.2f}"

  def __len__(self):
    return len(self._transactions)


# ---------------------------------------------------------
# 3. Child Classes
# ---------------------------------------------------------
class SavingsAccount(Account):

  def __init__(
      self,
      account_number: str,
      owner: str,
      balance: float = 0.0,
      interest_rate: float = 0.05,
  ):
    super().__init__(account_number, owner, balance)
    self.interest_rate = interest_rate

  def deposit(self, amount: float):
    if amount <= 0:
      raise InvalidTransactionError("Deposit amount must be greater than 0!")
    self._balance += amount
    self._transactions.append(f"Deposit: +${amount:.2f}")

  def withdraw(self, amount: float):
    if amount <= 0:
      raise InvalidTransactionError("Withdrawal amount must be greater than 0!")
    if amount > self._balance:
      raise InsufficientFundsError(
          f"Insufficient balance! Only ${self._balance:.2f} is available."
      )
    self._balance -= amount
    self._transactions.append(f"Withdraw: -${amount:.2f}")

  def calculate_interest(self):
    interest = self._balance * self.interest_rate
    self._balance += interest
    self._transactions.append(f"Interest Added: +${interest:.2f}")
    return interest


class CheckingAccount(Account):

  def __init__(
      self,
      account_number: str,
      owner: str,
      balance: float = 0.0,
      overdraft_limit: float = 500.0,
  ):
    super().__init__(account_number, owner, balance)
    self.overdraft_limit = overdraft_limit

  def deposit(self, amount: float):
    if amount <= 0:
      raise InvalidTransactionError("Deposit amount must be greater than 0!")
    self._balance += amount
    self._transactions.append(f"Deposit: +${amount:.2f}")

  def withdraw(self, amount: float):
    if amount <= 0:
      raise InvalidTransactionError("Withdrawal amount must be greater than 0!")
    if amount > (self._balance + self.overdraft_limit):
      raise InsufficientFundsError(
          f"Withdrawal exceeds the overdraft limit (${self.overdraft_limit:.2f})!"
      )
    self._balance -= amount
    self._transactions.append(f"Withdraw: -${amount:.2f}")

  def calculate_interest(self):
    return 0.0  # Checking accounts do not earn interest.


# ---------------------------------------------------------
# 4. Bank Class
# ---------------------------------------------------------
class Bank:

  def __init__(self, name: str):
    self.name = name
    self.__accounts = {}

  def add_account(self, account: Account):
    if account.account_number in self.__accounts:
      raise InvalidTransactionError("This account number already exists!")
    self.__accounts[account.account_number] = account

  def get_account(self, account_number: str) -> Account:
    acc = self.__accounts.get(account_number)
    if acc is None:
      raise InvalidTransactionError(
          f"Account number {account_number} was not found!"
      )
    return acc

  def transfer(self, from_acc_num: str, to_acc_num: str, amount: float):
    try:
      sender = self.get_account(from_acc_num)
      receiver = self.get_account(to_acc_num)

      # Withdraw from the sender and deposit into the receiver.
      sender.withdraw(amount)
      receiver.deposit(amount)
      print(
          f"✅ Successfully transferred ${amount:.2f} from [{from_acc_num}] to [{to_acc_num}]!"
      )

    except (InsufficientFundsError, InvalidTransactionError) as e:
      print(f"❌ Transfer failed: {e}")


# ---------------------------------------------------------
# Testing Code
# ---------------------------------------------------------
bank = Bank("Seavik Bank")

while True:
  print("\n" + "=" * 45)
  print(f"🏦 {bank.name}")
  print("=" * 45)
  print("1. Create an account")
  print("2. Deposit money")
  print("3. Withdraw money")
  print("4. Transfer money")
  print("5. Calculate interest")
  print("6. View account information")
  print("7. Exit")

  choice = input("Choose an option (1-7): ").strip()

  try:
    if choice == "1":
      account_type = input(
          "Choose an account type (1. Savings, 2. Checking): "
      ).strip()
      account_number = input("Enter the account number: ").strip()
      owner = input("Enter the account owner's name: ").strip()
      balance = float(input("Enter the initial balance: "))

      if account_type == "1":
        account = SavingsAccount(account_number, owner, balance)
      elif account_type == "2":
        account = CheckingAccount(account_number, owner, balance)
      else:
        print("❌ Invalid account type!")
        continue

      bank.add_account(account)
      print("✅ Account created successfully!")

    elif choice == "2":
      account = bank.get_account(input("Enter the account number: ").strip())
      amount = float(input("Enter the deposit amount: "))
      account.deposit(amount)
      print(f"✅ Successfully deposited ${amount:.2f}!")

    elif choice == "3":
      account = bank.get_account(input("Enter the account number: ").strip())
      amount = float(input("Enter the withdrawal amount: "))
      account.withdraw(amount)
      print(f"✅ Successfully withdrew ${amount:.2f}!")

    elif choice == "4":
      from_account = input("Sender's account number: ").strip()
      to_account = input("Receiver's account number: ").strip()
      amount = float(input("Enter the transfer amount: "))
      bank.transfer(from_account, to_account, amount)

    elif choice == "5":
      account = bank.get_account(input("Enter the account number: ").strip())
      interest = account.calculate_interest()
      print(f"✅ Interest added: ${interest:.2f}")
      print(f"New balance: ${account.balance:.2f}")

    elif choice == "6":
      account = bank.get_account(input("Enter the account number: ").strip())
      print(account)
      print(f"Number of transactions: {len(account)}")

    elif choice == "7":
      print("Thank you for using our banking service!")
      break

    else:
      print("❌ Invalid choice! Please choose a number from 1 to 7.")

  except ValueError:
    print("❌ Please enter a valid number!")
  except (InsufficientFundsError, InvalidTransactionError) as error:
    print(f"❌ {error}")