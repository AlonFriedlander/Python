import matplotlib


#print('hello world!')
#x = int(input("type a number"))
#print(x)
#if x > 0:
#   print(x,"is bigger")
#else:
#   print(x,"smaller")
#for i in range(10):
#   print(i)

#ages = [3, 4, 5, 6, 7, 8, 9]
#for i in ages:
#print(i)
# b = 3
# while b > 0:
#     print(b)
#     b = int(input("type a value for b"))

# def get_sum(s, c):
#     return s + c
#
# print(get_sum(5,4))
#
# my_list = [1,2,3,'hello',True]
# print(my_list)
#
# my_range = range(2,7)
# print(list(my_range))
#
# my_dict = {'name': 'Alice', 'age': 30}
#
# print('name' in my_dict)
# print('city' in my_dict)
# print('Alice' in my_dict.values())
#
# def is_adult(age):
#     return True if age > 18 else False
#
# print(is_adult(19))

# from enum import Enum
#
#
# class Color(Enum):
#     RED = 1
#     GREEN = 2
#     BLUE = 3


# print(Color.RED)
# print(Color.RED.value)

# for color in Color:
#     print(color.name)

# items = ["Roger", 1, "Syd", True]
#
# print(items[0:2])
# print(len(items))
# items.append("test")
# print(len(items))
# print(items)
#
# items.extend(["test"])
# print(len(items))
# print(items)

# dog = {'name': 'roger' , 'age': 8}
# print(dog.items())
# print(dog.values())
# print(dog.keys())

# set1 = {"Roger", "Syd"}
# set2 = {"R"}
#
# print(set1 > set2) # True

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         print(self.name + " says: woof")
#
#     def birthday(self):
#         self.age += 1
#         print(self.name + " is now " + str(self.age))
#
# dog1 = Dog("avi",6)
# dog1.bark()
# print(dog1.age)
# dog1.birthday()
# dog1.birthday()
#
# class Labrador(Dog):
#     def fetch(self):
#         print(self.name + " fetching")
#
# labrador1 = Labrador("moshe" , 3)
# labrador1.bark()
# labrador1.fetch()
# print(labrador1.name)

# import dog
# dog.bark()

from dog import bark
bark()