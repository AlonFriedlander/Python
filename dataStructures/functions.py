from collections import Counter


def remove_strings_list(list):
    #using list comprehension [output forCollection condition]
    return [item for item in list if isinstance(item, str)]


def count_letters_to_dict(text):
    dict_count = {}
    for char in text:
        if char in dict_count:
            dict_count[char] += 1
        else:
            dict_count[char] = 1
    return dict_count


# advance
def count_letters_to_dict2(text):
    dict_count = Counter(text)
    return dict_count

def same_element(list1, list2):
    return[elem for elem in list1 if elem in list2]

def left_rotate(list,n):
    return list[n:] + list[:n]

def print_second_element(list):
    while list:
        print(list.pop(1))
        if not list:
            break
        list.pop(0)

def find_min_max_from_dict(dict):
    print(max(dict, key=lambda k: dict[k]))
    print(max(dict,key=dict.get))
    print(min(dict, key=lambda k: dict[k]))
