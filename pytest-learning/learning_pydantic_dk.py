from pydantic import BaseModel,Field,ValidationError

# class Engineer(BaseModel):
#     name:str
#     age:int
#     salary:int

# dhruva=Engineer(name="DHRUVA",age=24,salary=25000)
# d1=Engineer(name="DHRUVA",age="twenty four",salary=25000) #ValidationError: 1 validation error for Engineer age
#   #Input should be a valid integer, unable to parse string as an integer
#  # You wrote no if statement and no raise, and Pydantic told you exactly which field was wrong and why. This is the same job as your Engineer setter and check_positive decorator, done from one line of type hints.#
# print(dhruva.name)
# print(dhruva)
# print(d1)




# class Engineer(BaseModel):
#     name:str
#     age:int
#     salary:float
# d1=Engineer(name="dhruva",age="24",salary=25000)
# print(d1)

# Case 2 (age="abc") should give an error. "abc" can't become an integer, so Pydantic rejects it with a ValidationError. That's the checking we wanted.

# Case 1 (age="24", salary=50000) should not give an error. Pydantic accepts it and prints:

# name='Dhruva' age=24 salary=50000.0
# Why Case 1 works: type coercion

# Pydantic doesn't just check types, it also tries to convert a value to the declared type when the conversion is safe. This is called coercion:

# "24" is a string, but it clearly represents the number 24, so Pydantic converts it to the int 24
# 50000 is an int, but the field says float, so Pydantic converts it to 50000.0

# Look at the printed result: age=24 has no quotes (an int now, not a string), and salary=50000.0 has a decimal point (a float now).

# This is useful in practice. Data coming from web requests often arrives as strings (for example, "24" from a URL or form field), and Pydantic turns it into the right type for you. When the conversion is impossible, like "abc" to an int, it raises the error.


# New things here:

# Field(...) lets you attach extra rules to a field, beyond its type.
# min_length=2: the string must have at least 2 characters.
# gt=0: "greater than 0", so negative salary and zero are both rejected.
# ge=18: "greater than or equal to 18".
# le=65: "less than or equal to 65".


# class Product(BaseModel):
#     name:str =  Field(min_length=2)
#     price:float = Field(gt=0)
#     quantity:int = 1

# p1=Product(name="laptop",price=50000)
# print(p1)
# p2=Product(name="lap",price=-3000,quantity=2)

# print(p2)


#  In a real app, you don't want one bad input to crash the whole program. You want to catch the error and handle it, such as sending back a friendly message. Python does this with try / except

# class Product(BaseModel):
#     name:str =  Field(min_length=2)
#     price:float = Field(gt=0)
#     quantity:int = 1
#     description:str | None=None
#     # Some data may legitimately be missing, such as a middle name or a discount. You mark that with None
# #     str | None means "either a string or None". The | reads as "or".
# #    = None is the default, so the field can be left out.
# p1=Product(name="laptop",price=50000)
# print(p1)
# try:
#     p2=Product(name="lap",price=-3000,quantity=2)
#     print(p2)
# except ValidationError as e:
#     print("invalid product data")
#     print(e)

# print("program is still running")

# print(p1.model_dump())
# print(p1.model_dump_json())

# data = {"name": "mouse", "price": "799", "quantity": "3"}
# p3=Product(**data)
# print(p3)
# Real data often contains other data. An engineer has an address, and an address has its own fields. In Pydantic, you use one model as the type of a field in another:

class Address(BaseModel):
    city:str
    pincode:int = Field(ge=100000, le=999999)
class Engineer(BaseModel):
    name:str
    age:int = Field(ge=18,le=65)
    address:Address

class Team(BaseModel):
    team_name:str
    members:list[Engineer]  

data = {
    "team_name": "Backend",
    "members": [
        {"name": "dhruva", "age": 24,
         "address": {"city": "Bengaluru", "pincode": "560001"}},
        {"name": "rahul", "age": 10,
         "address": {"city": "Delhi", "pincode": "110001"}},
    ]
}


try:
    team=Team(**data)
    print(team.members[0].name)
    print(team.members[0].address.city)
except ValidationError as err:
    print("data is incorrect")
    print(err)
