import logging

# logging.basicConfig(level=logging.DEBUG, filename="log.log",filemode="w",
#                     format="%(asctime)s - line num = %(lineno)d - %(levelname)s - %(message)s")
#
# logger = logging.getLogger(__name__)
#
# handler = logging.FileHandler('test.log')
# formatter = logging.Formatter("%(asctime)s - line num = %(lineno)d - %(levelname)s - %(message)s")
# handler.setFormatter(formatter)
#
# logger.addHandler(handler)
#
# logger.info("test the custom logger")
#
#
# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")
#
# x = 2
# logging.debug(f"the value of x is {x}")
#
# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.error("ZeroDivisionError", exc_info=True)
#     logging.exception("ZeroDivisionError")


#...............................................

# logging.basicConfig(level=logging.DEBUG)
#
# logger = logging.getLogger("blablabla")
#
# file_handler = logging.FileHandler("test.log")
# file_handler.setLevel(logging.DEBUG)
# logger.addHandler(file_handler)
#
# logger.debug("hey there")


def foo(l=[]):
    l.append(1)
    print(l)



def foo2(x = 0):
    x+=1
    print(x)

def foo3(x,dict = {}):
    dict[x] = x

    print(dict)


foo()
foo()
foo2()
foo2()
foo3(1)
foo3(2)


def foo4():
    l = []
    l.append(1)
    print(l)

foo4()
foo4()


def foo5(l=None):
    if l is None:
        l = []
    l.append(1)
    print(l)

foo5()
foo5()