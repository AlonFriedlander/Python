import functions


# functions.f("hi")
# print(functions.add(4,5))

# def multiply(num1):
#     def inner(num2):
#         return num1 * num2
#     return inner
#
#
# m1 = multiply(1)
# print(m1(10))
# m2 = multiply(2)
# print(m2(10))
# m3 = multiply(3)
# print(m3(10))

words = ["hey", "how", "are", "you", "?"]
to_remove = ["hey", "you"]

print(functions.remove_words(words,to_remove))

string_numbers = ["5", "10", "2", "7", "1"]
print(functions.sort_string(string_numbers))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(functions.sqaure_evens_numbers(numbers))

products = {"apple": 10, "banana": 5, "orange": 7}
print(functions.ten_precent_discount(products))

print(functions.gemetria_calc("שלומ"))
print(functions.gemetria_calc("אינפיניטילאבס"))