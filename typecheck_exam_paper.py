from typing import *

# wrongly typed variable
a: str = 1

b: int = 2

# Wrong argument type
def plus_one_bad(arg: str) -> int:
    return arg + 1

# Wrong return type
def plus_one_bad_2(arg: int) -> str:
    return arg + 1

l: List[int] = []

# Adding wrong type to generic
l.append(1)

# Referring to a type further down
f1: Optional[F] = None

class F:
    ...
