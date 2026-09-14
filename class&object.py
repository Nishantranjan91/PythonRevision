# class Business:
#     a = "hello I am attribute"
#     def hello():
#         print("hello I am a method")
# obj = Business()
# print(obj.a)        




# class Business:
#     a = "hello I am attribute"
#     def hello():
#         print("hello I am a method")
# obj = Business() # obj becomes an object who can access anything
# obj2 = Business()
# print(obj.a) 
# Business.hello()






class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):     # Instance method
        self.balance += amount

    def show_balance(self):        # Instance method
        print("Balance:", self.balance)


account = BankAccount(1000)

account.deposit(500)
account.show_balance()