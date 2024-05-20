# x:str = 1

# def add_numbers(a:int,b:int,c:int) -> int:
#     return a + b + c
#
# x = add_numbers(1,2,4)
# print(x)

from typing import List, Callable, Optional,Dict,Set,Any,Tuple, Sequence

x: List[List[int]] = []

Vector = List[float]


def foo(v: Vector) -> Vector:
    print(v)
    return v


foo([1.1, 2.3, 5.7])

def add(x:int, y: int) -> int:
    return x+y

def foo2(func:Callable[[int,int],int]) -> None:
    func(1,2)

foo2(add)