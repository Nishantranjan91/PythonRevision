#Basic Abstraction using ABC
# from abc import ABC, abstractmethod
# from abc import ABC, abstractmethod

# class Animal(ABC):

#     @abstractmethod
#     def sound(self):
#         pass


# class Dog(Animal):

#     def sound(self):
#         print("Dog barks")


# dog = Dog()
# dog.sound()




# Abstraction with Car
# from abc import ABC, abstractmethod

# class Car(ABC):

#     @abstractmethod
#     def start(self):
#         pass


# class BMW(Car):

#     def start(self):
#         print("BMW starts with a button")


# class Tesla(Car):

#     def start(self):
#         print("Tesla starts automatically")


# car1 = BMW()
# car1.start()

# car2 = Tesla()
# car2.start()




# Abstraction with Payment System
# from abc import ABC, abstractmethod

# class Payment(ABC):

#     @abstractmethod
#     def pay(self, amount):
#         pass


# class CreditCard(Payment):

#     def pay(self, amount):
#         print(f"Paid ₹{amount} using Credit Card")


# class UPI(Payment):

#     def pay(self, amount):
#         print(f"Paid ₹{amount} using UPI")


# payment1 = CreditCard()
# payment1.pay(1000)

# payment2 = UPI()
# payment2.pay(500)



# Abstraction with Database
# from abc import ABC, abstractmethod

# class Database(ABC):

#     @abstractmethod
#     def connect(self):
#         pass

#     @abstractmethod
#     def disconnect(self):
#         pass


# class MySQL(Database):

#     def connect(self):
#         print("Connected to MySQL")

#     def disconnect(self):
#         print("Disconnected from MySQL")


# db = MySQL()

# db.connect()
# db.disconnect()




# Practical Example — Notification System
from abc import ABC, abstractmethod

class Notification(ABC):

    @abstractmethod
    def send(self, message):
        pass


class Email(Notification):

    def send(self, message):
        print(f"Email sent: {message}")


class SMS(Notification):

    def send(self, message):
        print(f"SMS sent: {message}")


class WhatsApp(Notification):

    def send(self, message):
        print(f"WhatsApp message sent: {message}")


notifications = [
    Email(),
    SMS(),
    WhatsApp()
]

for notification in notifications:
    notification.send("Your order has been shipped!")