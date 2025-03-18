# type hints

def get_full_name(first_name: str, last_name: str):
    return first_name.title() + " " + last_name.title()

print(get_full_name("Arturo", "Marin"))

def get_name_with_age(name: str, age: int):
    return "Name: " + name.title() + "  Age: " + str(age)

print(get_name_with_age("Arturo", 22)) 

# List

items = ["hola", "arturo", "marin"]

def process_items(items: list[str]):
    for item in items:
        print(item)

print(process_items(items))

# Tuple and Set

items2 = (2, "hola", 6)
items3 = (20, 40, 17)

def process_items(items2: tuple[int, str, int], items3: set[bytes]):
    return items2, items3

print(process_items(items2, items3))

# Dict

prices = {"Ferrari": 100000}

def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

print(process_items(prices))

# Union

def process_item(item: int | str):
    print(item)

process_item("hola") # 0 process_item(68)

# Possibly none

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

say_hi()

# Las clases como tipos

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name

# Pydantic models
# Pydantic es una biblioteca de Python para realizar la validación de datos.

from datetime import datetime

from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
# > User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)
# > 123