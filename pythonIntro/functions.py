def count_char(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count


def flip_number(number):
    string_num = str(number)
    flipped = string_num[::-1]  #[start:stop:step]
    return int(flipped)


def is_leap_year(year):
    return ((year % 4) == 0) and ((year % 400) == 0 or (year % 100) != 0)


def password_complexity(password):
    if len(password) < 8:
        return False

    if not (any(char.isupper() for char in password) and any(char.islower() for char in password) and
            any(char.isdigit() for char in password)):
        return False

    special_chars = {'@', '#', '%', '&'}
    if not any(char in special_chars for char in password):
        return False

    return True

def money(amount):
    banknotes = [200, 100, 50, 20]
    coins = [10, 5, 2, 1]

    # Initialize variables to store the breakdown
    bills_count = {}
    coins_count = {}

    # Break down the amount into bills
    for banknote in banknotes:
        count = amount // banknote
        if count > 0:
            bills_count[banknote] = count
            amount -= count * banknote

    # Break down the remaining amount into coins
    for coin in coins:
        count = amount // coin
        if count > 0:
            coins_count[coin] = count
            amount -= count * coin

    # Print the breakdown
    print("Bills:")
    for banknote, count in bills_count.items():
        print(f"{count}x {banknote} NIS")

    print("\nCoins:")
    for coin, count in coins_count.items():
        print(f"{count}x {coin} NIS")