
# class student:
#     'This is a student class'
#     def __init__(self,
#             name,
#             rollno):
#         self.name = name
#         self.rollno = rollno

#     def setage(self,age):
#         self.age = age

#     def setmarks(self,marks):
#         self.marks = marks

#     def display(self):
#         'This is display method'
#         print("name:-",self.name,"roll no:-",self.rollno,"\n"\
#             "age:-",self.age,"marks:-",self.marks)


# std1 = student("aparna",1)
# std1.setage(12)
# std1.setmarks(120)
# std1.display()

# print(std1.__class__)
# print(student.__doc__)
# print(student.display.__doc__)

# --------------------------------------------
# from typing import Any


# class decorator_class:
#     def __init__(self, orgFunc):
#         self.func = orgFunc
    
#     def __call__(self, *args: Any, **kwargs: Any) -> Any:
#         print("inside wrapper function")
#         self.func(*args, **kwargs)

# @decorator_class
# def display():
#     print("inside display function")

# display()

# @decorator_class
# def displayInfo(name, age):
#     print(f"display_info with args: {name} & {age}")

# displayInfo('Devin', 28)
# ---------------------------------------------
# __call__ dunder method

# class Product: 
#     def __init__(self): 
#         print("Instance Created") 
  
#     # Defining __call__ method 
#     def __call__(self, a, b): 
#         return(a * b) 
  
# # Instance created 
# ans = Product() 
  
# # __call__ method will be called 
# print(ans(10, 20))
# ---------------------------------------------

# class employee:
#     raise_amt = 1.04

#     def __init__(self,first,last,pay):
#         self.first = first
        
#         self.last = last
#         self.mail = first+'.'+last+"@gmail.com"
#         self.pay = pay
        
#     def raiseamt(self):
#         return f"{self.pay*self.raise_amt}"

#     @classmethod
#     def setRaiseAmt(cls, amt):
#         cls.raise_amt = amt

# emp1 = employee('hari', 'kri', 10000)

# print(emp1.raiseamt())
# print(emp1.raise_amt)

# employee.setRaiseAmt(1.06)

# print(emp1.raise_amt)
# print(emp1.raiseamt())
# ---------------------------

# class employee:
#     raise_amt = 1.04
#     def __init__(self,first,last,pay):
#         self.first = first
        
#         self.last = last
#         self.mail = first+'.'+last+"@gmail.com"
#         self.pay = pay
        
#     def raiseamt(self):
#         return f"{self.pay*1.04}"

#     @classmethod
#     def createEmployee(cls, str):
#         a, b, c = str.split('-')
#         return cls(a, b, c)

# str1 = 'dev-sam-32000'

# a, b, c = str1.split('-')
# emp2 = employee(a, b, c)

# emp3 = employee.createEmployee(str1) 
# print(emp3.first, emp3.last, emp3.pay)

# ------------------------------------------
import datetime

# def checkWorkingDay(day):
#     if datetime.date.isoweekday(day) == 6 or datetime.date.isoweekday(day) == 7:
#         print("It's a holiday")
#     else:
#         print("it's a working day.")

# d = datetime.date(2023, 11, 5)
# checkWorkingDay(d)

# class employee:
#     raise_amt = 1.04
#     def __init__(self,first,last,pay):
#         self.first = first
        
#         self.last = last
#         self.mail = first+'.'+last+"@gmail.com"
#         self.pay = pay
        
#     def raiseamt(self):
#         return f"{self.pay*1.04}"

#     @staticmethod
#     def checkWorkingDay(day):
#         if datetime.date.isoweekday(day) == 6 or datetime.date.isoweekday(day) == 7:
#             return "It's a holiday"
#         else:
#             return "it's a working day."
    

# emp1 = employee('ram', 'hari', 34444)

# dt = datetime.date(2023, 11, 11) #yyyy,mm,dd
# datetime.date.weekday(dt) - 
# print(employee.checkWorkingDay(dt))
# print(emp1.checkWorkingDay(dt)) #also works with objects
# ---------------------------------------------------
class employee:
    def __init__(self, name, salary, projName) -> None:
        self.name = name
        self.salary = salary
        self.projName = projName

    def work(self):
        req = self.gather_requirement(self.projName)

        for task in req:
            print(f"{task} is completed.")
    
    @staticmethod
    def gather_requirement(proj):
        if proj == 'ABC projects':
            req = ['task1', 'task2', 'task3']
        else:
            req = ['task1']
        return req

# emp1 = employee('varna', 100000, 'project')
emp1 = employee('varna', 100000, 'ABC projects')
emp1.work()