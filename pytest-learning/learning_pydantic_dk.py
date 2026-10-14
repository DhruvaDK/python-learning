from pydantic import BaseModel,Field,ValidationError,field_validator

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

# class Address(BaseModel):
#     city:str
#     pincode:int = Field(ge=100000, le=999999)
# class Engineer(BaseModel):
#     name:str
#     age:int = Field(ge=18,le=65)
#     address:Address

# class Team(BaseModel):
#     team_name:str
#     members:list[Engineer]  

# data = {
#     "team_name": "Backend",
#     "members": [
#         {"name": "dhruva", "age": 24,
#          "address": {"city": "Bengaluru", "pincode": "560001"}},
#         {"name": "rahul", "age": 10,
#          "address": {"city": "Delhi", "pincode": "110001"}},
#     ]
# }


# try:
#     team=Team(**data)
#     print(team.members[0].name)
#     print(team.members[0].address.city)
# except ValidationError as err:
#     print("data is incorrect")
#     print(err)


# class Engineer(BaseModel):
#     name:str
#     age:int

#     @field_validator("name")
#     @classmethod
#     def name_check(cls,value):
#         if any(ch.isdigit() for ch in value):
#             raise ValueError("name cannot digits")
#         return value
# d1=Engineer(name="dhruva5",age="24")
# print(d1)

# What each new piece does

# @field_validator("name") is a decorator, the same idea as your @timer. It tells Pydantic: "whenever the name field is being validated, also run the function below." The string "name" must match the field name exactly. If you misspell it, Pydantic raises an error when the class is defined.

# @classmethod goes right under it. A classmethod belongs to the class instead of one object, so its first parameter is cls instead of self. You don't need more than that for now. Whenever you write a field validator, write both decorators together.

# value is the incoming data for that field. By the time your function runs, Pydantic has already checked the type, so value is guaranteed to be a str here.

# ch.isdigit() is a built-in string method. It returns True if the character is a digit ("7".isdigit() is True, "a".isdigit() is False).

# any(... for ch in value) uses the generator-expression idea from your generators lesson. any() is a built-in that returns True if at least one item in the sequence is True. So the whole line asks: "is any character in this name a digit?"

# raise ValueError(...) is the same raise from your Engineer setter. Pydantic catches it and turns it into a ValidationError for you.

# return value is the most important line. Whatever you return becomes the stored value. This is the same lesson as return res in your decorators. If you forget it, the function returns None and name gets stored as None.





# class Engineer(BaseModel):
#     name:str
#     age:int

#     @field_validator("name")
#     @classmethod
#     def clean_data(cls,value):
#         return value.strip().title()
# d1=Engineer(name="dhruva d k",age="24")
# print(d1)


# With this validator, " dhruva dk " is stored as "Dhruva Dk". It trims the spaces with .strip() and capitalizes each word with .title().

class Product(BaseModel):
    name:str
    price:float = Field(gt=0)

    @field_validator("name")
    @classmethod
    def check_name(cls,value):
        if value.strip()=="":
            raise ValueError("name cannot be empty")
        
        return value.strip().title()
# Case 1: should work and clean the name
try:
    p1 = Product(name="  laptop  ", price=50000)
    print(p1)                      # name='Laptop' price=50000.0
except ValidationError as err:
    print("case 1 failed:", err)

# Case 2: validator should reject the empty name
try:
    p2 = Product(name="   ", price=100)
    print(p2)
except ValidationError as err:
    print("case 2 failed:", err)

# Case 3: Field rule should reject the negative price
try:
    p3 = Product(name="mouse", price=-5)
    print(p3)
except ValidationError as err:
    print("case 3 failed:", err)