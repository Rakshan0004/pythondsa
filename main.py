number = 10
decimal: float = 20.0
name: str = 'Bob'
age: int = 1


str1 = "hello"
str2 = "world"
def func():
    pass

#print(type(func))

str1 = "hello"

new_str = str1.__len__()
#print(new_str)


#every thing in python is objects

class Counter:
    def __init__(self):
        self.value = 1
        
    def count_down(self):
        self.value -= 1
    
    def __str__(self):
        return f"Count={self.value}"

    # This is "Operator Overloading".
    # By defining __add__, we tell Python what to do when we use the '+' sign 
    # between two Counter objects (e.g., count1 + count2).
    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        else:
            raise Exception("invalid type")
        # We return the sum of the 'value' attributes of both objects
       

    def count_up(self):
        self.value += 1

count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_down()

print(count1,  count2)
print(count1 + count2)
