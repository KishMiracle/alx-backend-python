class a:
    def __init__(self, value):
        self.value = value
# Define a function that takes an instance of class 'A' and returns 1
def return_one_from_a(obj: a) -> int:
    return 1
# Define a function that takes an instance of class 'pi' and returns 3.14
class pi:
    def __float__(self, value):
        self.value = value
def return_float_from_a(obj: pi) -> float:
    return 3.14
# Define a function that takes an instance of class 'bool' and returns w
class pi:
    def __float__(self, value):
        self.value = value

# Define a function that takes an instance of class 'A' and returns 1
def return_float_from_a(obj: pi) -> float:
    return 3.14
