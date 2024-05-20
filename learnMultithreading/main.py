# import threading
# import time
#
#
# def eat_breakfast():
#     time.sleep(3)
#     print("you eat breakfast")
#
#
# def drink_coffe():
#     time.sleep(4)
#     print("you drink coffe")
#
#
# def study():
#     time.sleep(5)
#     print("you finish study")
#
# x = threading.Thread(target=eat_breakfast)
# x.start()
#
# y = threading.Thread(target=drink_coffe)
# y.start()
#
# z = threading.Thread(target=study)
# z.start()
#
# x.join()
# y.join()
# z.join()
#
# print(threading.active_count())
# print(threading.enumerate())
# print(time.perf_counter())


# def longest_common_prefix(strs):
#     for i, char in enumerate(strs[0]):
#         for string in strs[1:]:
#             if i >= len(string) or string[i] != char:
#                 return strs[0][:i]
#     return ""
#
# strings = ["flower", "flowing", "floor"]
# print(longest_common_prefix(strings))  # Output: "flo"


import threading
import time

# x = 8192
# lock = threading.Lock()
# def double():
#     global x
#     lock.acquire()
#     while x < 16384:
#         x *= 2
#         print(x)
#         time.sleep(1)
#     print("reached the maximum")
#     lock.release()
#
# def halve():
#     global x
#     lock.acquire()
#     while x> 1:
#         x /= 2
#         print(x)
#         time.sleep(1)
#     print("reached the minimum")
#     lock.release()
#
# t1 = threading.Thread(target=halve)
# t2 = threading.Thread(target=double)
#
# t1.start()
# t2.start()

semaphore = threading.BoundedSemaphore(value=5)

def access(thread_number):
    print("{} im try to access".format(thread_number))
    semaphore.acquire()
    print("{} acquire access".format(thread_number))
    time.sleep(10)
    print("{} relaseing".format(thread_number))
    semaphore.release()

for thread_number in  range(1 , 11):
    t = threading.Thread(target=access,args=(thread_number,))
    t.start()
    time.sleep(1)
