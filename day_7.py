#banck account withdrawal

class BankAccount:
    def __init__(self):
        self.__balance = 5000
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid Deposit Amount")
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid Withdrawal Amount")
        elif amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient Balance")
    def get_balance(self):
        return self.__balance

b = BankAccount()

b.deposit(2000)
b.withdraw(3000)
b.withdraw(5000)
print(b.get_balance())

#password protection

class User:
    def __init__(self):
        self.__password = ""
    def set_password(self, password):
        self.__password = password
    def check_password(self, password):
        if password == self.__password:
            print("Login Successful")
        else:
            print("Wrong Password")

u = User()
u.set_password("python123")
u.check_password("python123")
u.check_password("hello")


def func1(*args):
    print("printing values:")
    for i in args:
        print(i)
func1(20,40,60)
func1(80,100)