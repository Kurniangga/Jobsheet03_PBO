class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount>0:
            self.__balance += amount
            print(f"{amount} telah ditambahkan ke akun {self.__owner}.")
        else:
            print("Jumlah deposit harus lebih dari 0.")
    
    def withdraw(self, amount):
        if amount<=self.__balance:
            self.__balance -= amount
            print(f"{amount} telah ditarik dari akun {self.__owner}.")
        else:
            print("Saldo tidak mencukupi.")

    def get_balance(self):
        return self.__balance
    
if __name__=="__main__":
    alice_account = BankAccount(owner="Alice", balance=1000)
    alice_account.deposit(500)
    alice_account.deposit(-100)

    alice_account.withdraw(300)
    alice_account.withdraw(2000)

    current_balance = alice_account.get_balance()
    print(f"Saldo terakhir di akun {alice_account._BankAccount__owner} : {current_balance}")
    
