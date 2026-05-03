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
        self.value = 0
        
    def count_down(self):
        self.value -= 1
    
    def __str__(self):
        return f"Count={self.value}"

    def __add__(self, other):
        return self.value + other.value

    def count_up(self):
        self.value += 1

count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_down()

print(count1,  count2)
print(count1 + count2)
