import logging
valus = [10,6,"hello",4,0,5,6]
for val in valus:
    try:
        print(10/int(val))
    except (ZeroDivisionError,ValueError) as e:
        pass
    except AttributeError as e:
        print(e)
    except Exception as e:
        logging.exception(e)
