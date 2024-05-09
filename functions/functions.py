def f1(func):
    def wrapper(*args,**kwargs):
        print("started")
        val = func(*args,**kwargs)
        print("end")
        return val
    return wrapper

 #every time we call f it call f1 and pass f as a parameter
@f1
def f(a,b=9):
    print(a,b)
@f1
def add(x,y):
    return x + y

def remove_words(word_list, words_to_remove):
    filter_list = filter(lambda word: word not in words_to_remove, word_list)
    return list(filter_list)

def sort_string(string):
    return sorted(string,key=lambda x: int(x))

def sqaure_evens_numbers(list):
    return [x**2 for x in list if x % 2 == 0]

#dict = {key: expression for (key,value) in iterable}
def ten_precent_discount(dict):
    return {product + "a":price * 0.9 for (product, price) in dict.items()}

gematria_table = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5,
    'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9, 'י': 10,
    'כ': 20, 'ל': 30, 'מ': 40, 'נ': 50, 'ס': 60,
    'ע': 70, 'פ': 80, 'צ': 90, 'ק': 100, 'ר': 200,
    'ש': 300, 'ת': 400
}

def gemetria_calc(word):
    return sum(gematria_table[char] for char in word)