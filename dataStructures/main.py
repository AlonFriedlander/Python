import functions



# x = 'DevOps'
# print(x[-1:-2])
# print(x[3:-1])
# print(x[::1])
# print(x[::3])
# print(x[1:2:3])
# print(x[::-1])
# print(x[1::-1])


print (functions.remove_strings_list([1, 'hello', 3.14, 'world', True, 'python']))
print(functions.count_letters_to_dict("aloaanlo"))
#advance
print(functions.count_letters_to_dict2("aloaanlo"))
print (functions.same_element([1,2,3,4,5,6],[1,3,4,7,9]))
print(functions.left_rotate([1,2,3,4,5], 2))
print(functions.print_second_element([1,2,3,4,5,6,7,8,9,10]))
functions.find_min_max_from_dict({'a': 10, 'b': 5, 'c': 15, 'd': 3})