# class parent:
#     def __init__(self):
#         print("in base")
    
# class child(parent):
#     def __init__(self):
#         print("in derived")

# # p1 = parent()
# c1 = child() #calls the base constr only if child has no constr
# so basically, only base has constr so child doesnt need one(except for additional info).
# ---------------------------------------------------------------
# single inheritance

# class employee:
#     raise_amt = 1.04
#     def __init__(self,first,last,pay):
#         self.first = first
#         self.last = last
#         self.mail = first+'.'+last+"@gmail.com"
#         self.pay = pay
        
#     def raiseamt(self):
#         return f"{self.pay*self.raise_amt}"
    
# # class dev(employee):
# #     pass

# # d = dev('varna', 'kar', 2343434) #calls the employee constr
# # print(d.raiseamt()) #raise_amt = 1.04,, 2437171.36

# class dev(employee):
#     raise_amt = 1.08

# d = dev('varna', 'kar', 2343434) #calls the employee constr
# print(d.raiseamt()) #raise_amt = 1.08, 2530908.72

# e = employee('hari', 'h', 34534534)
# print(e.raiseamt()) #35915915.36
# ---------------------------------------------------------------

# class employee:
#     raise_amt = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.mail = first+'.'+last+"@gmail.com"
#         self.pay = pay
        
#     def raiseamt(self):
#         return f"{self.pay*self.raise_amt}"
    
# class developer(employee):
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay) #calling base constr

#         self.progLang = prog_lang

#     def __str__(self) -> str:
#         return f"Developer details\n-------------------------\n\
# Name: {self.first} {self.last}\nSalary: {self.pay}\n\
# Programming Language: {self.progLang}"

# emp = employee('dev', 'hari', 40000)
# dev = developer('varna', 'kar', 200000, 'python')
# print(dev)
# ----------------------------------------------------
# mgr - add, delete, display

# class employee:
#     def __init__(self, first, last, pay, id):
#         self.first = first
#         self.last = last
#         self.mail = first+'.'+last+"@gmail.com"
#         self.pay = pay
#         self.id = id
        
#     def raiseamt(self):
#         return f"{self.pay*self.raise_amt}"
    
# class developer(employee):
#     def __init__(self, first, last, pay, id, prog_lang):
#         super().__init__(first, last, pay, id) #calling base constr
#         self.progLang = prog_lang
    
#     def displayDetails(self):
#         print(f"Name: {self.first} {self.last}\n\
# Employee id: {self.id}\n\
# Salary: {self.pay}\n\
# Programming Language: {self.progLang}\n\n")

# class manager(employee):
#     # def __init__(self, first, last, pay, id, dev):
#     #     super().__init__(first, last, pay, id)

#     #     self.team = []
#     #     self.team.append(dev)
#     def __init__(self, first, last, pay, id, dev=None):
#         super().__init__(first, last, pay, id)
#         self.team = [] if dev is None else dev            

#     def addMember(self, dev):
#         if dev not in self.team:
#             self.team.append(dev)
#             print("New member added\n------------------------------------\n")

#     def releaseMember(self, dev):
#         if dev in self.team:
#             self.team.remove(dev)
#             print("A member is released\n------------------------------------\n")

#     def displayTeamInfo(self):
#         if len(self.team) != 0:
#             for each in self.team:
#                 each.displayDetails()
#         else:
#             print("Manager has no team members")

# # driver
# dev1 = developer("hazal", 'bristan', 30000, 12, 'python')
# dev2 = developer("har", 'vista', 300000, 676, 'c++')
# dev3 = developer("vera", 'kar', 56000, 45, 'java')

# # mgr = manager('var', 'kar', '250000', 64, dev1)
# # mgr = manager('var', 'kar', '250000', 64, [dev1])
# mgr = manager('var', 'kar', '250000', 64)
# mgr.displayTeamInfo()
 
# mgr.addMember(dev2)
# mgr.addMember(dev3)
# # mgr.displayTeamInfo()

# mgr.releaseMember(dev3)
# # mgr.displayTeamInfo()

# print(isinstance(mgr, employee))
# print(issubclass(developer, employee))
# =================================================
# @property decorator

# class employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         # self.email = self.first+'.'+self.last+"@gmail.com"
#         self.pay = pay
#         self.id = id
    
#     @property
#     def fullName(self):
#         return f"{self.first} {self.last}"
    
#     @fullName.setter
#     def fullName(self, name):
#         print("inside setter")
#         self.first, self.last = name.split()
    
#     @fullName.deleter
#     def fullName(self):
#         self.first, self.last = None, None

#     @property
#     def mail(self):
#         return self.first+'.'+self.last+"@gmail.com"

# emp1 = employee('devin', 'mathew', 10000)

# emp1.first = 'david'

# print(emp1.first)
# print(emp1.mail)
# print(emp1.fullName)

# print(emp1.fullName) #devin mathew

# emp1.fullName = 'varna kar' # emp1.<<var_name>> should be same as the setter function name
# print(emp1.fullName) #varna kar

# del emp1.fullName
# print(emp1.fullName) #None None
# -----------------------------------------------------
# multi-level inheritance

class person:
    def display(self):
        print("this is person class")

class employee(person):
    def printing(self):
        print("this is employee of parent person")

class programmer(employee):
    def show(self):
        print("programmer class")

p1 = programmer()
p1.display() #this is person class
p1.printing() #this is employee of parent person
p1.show() #programmer class





















