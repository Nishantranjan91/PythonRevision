# #Different classes can have a method with the same name but different behavior
# class Dog:
#     def sound(self):
#         print("Dog says: Woof Woof")


# class Cat:
#     def sound(self):
#         print("Cat says: Meow")


# dog = Dog()
# cat = Cat()

# dog.sound()
# cat.sound()




# The same function can work with different types of objects.
class Dog:
    def sound(self):
        return "Woof"


class Cat:
    def sound(self):
        return "Meow"


def make_sound(animal):
    print(animal.sound())


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)




