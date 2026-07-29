

# ## recalled from old learning
# #
# # class Hero:
# #     def __init__(self):
# #         self.name="yash"
# #         self.age=45
# #         self.address="hassan"
# #     def act(self):
# #         print("he is a actor")
# #     def ranking(self):
# #         print("he is number 1 in India")
# # f1=Hero()
# # print(f1.name)
# # print(f1.age)
# # print(f1.address)
# # f1.act()
# # f1.ranking()

# # Learn this today
# class Engineer:
#     def __init__(self, name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary



#     def get_raise(self, percent):
#         self.salary = self.salary * (1 + percent/100)
#         return self.salary
# f1=Engineer()
# # Practice using it
# dhruva = Engineer("Dhruva", 23, 7)
# f1.get_raise("Dhruva", 23, 7)
# dhruva.get_raise(400)  # going from 7 to 40 LPA 😄
# print(dhruva)



## class and objects
# class student:
#     def __init__(self):
#         self.name="dhruva"
#         self.age=24
#     def study(self):
#         print("he is studying")
# f1=student()
# f1.study()
# print(f1.name)
# print(f1.age)



# class Engineer:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def __repr__(self): ###__repr__ is a built-in dunder method that Python already knows about. But the behaviour inside it is 100% yours to define.

#         return f"Engineer(Name:{self.name},Age:{self.age},Salary:{self.salary})"
#     def salary_jump(self,percent):
#         self.salary=self.salary*(1+percent/100)
#         return self.salary
# dhruva=Engineer("Dhruva",24,7)
# print(dhruva)
# dhruva.salary_jump(500)
# print(dhruva)


##Inheritence

# class Engineer:
#     def __init__(self,name,age,salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#     def __repr__(self): ###__repr__ is a built-in dunder method that Python already knows about. But the behaviour inside it is 100% yours to define.

#         return f"Engineer(Name:{self.name},Age:{self.age},Salary:{self.salary})"
#     def salary_jump(self,percent):
#         self.salary=self.salary*(1+percent/100)
#         return self.salary
#     def introduce(self):
#         return f"Engineer(my name is : {self.name} and my age is :{self.age})"

# class AI_Engineer(Engineer):
#     def __init__(self,name,age,salary,ai_model):
#         super().__init__(name,age,salary)
#         self.ai_model=ai_model
#     def __repr__(self):
#         return f"AI_Engineer(Name:{self.name},age:{self.age},salary:{self.salary},{self.name} is building an {self.ai_model} model)"
    
# class Backend(Engineer):
#     def __init__(self,name,age,salary,framework):
#         super().__init__(name,age,salary)
#         self.framework=framework
#     def __repr__(self):
#         return f"Backend(Name:{self.name},age:{self.age},salary:{self.salary},framework:{self.framework})"


# dhruva=Engineer("Dhruva",24,7)
# print(dhruva)

# dhruva=AI_Engineer("Dhruva",24,7,"ChatGPT")
# print(dhruva)
# dhruva.salary_jump(600)
# print(dhruva)
# print(dhruva.introduce())
# dhruva=Backend("Dhruva",24,7,"Django")
# print(dhruva)
