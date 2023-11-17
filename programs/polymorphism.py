# method overriding
# class parent:
#     def __init__(self, name, eye_color) -> None:
#         self.name = name
#         self.eye_color = eye_color
    
#     def display_info(self):
#         print(f"{self.name} has {self.eye_color} eye colour.")

# class child(parent):
#     def __init__(self, name, eye_color, toys):
#         super().__init__(name, eye_color)
#         self.toys = toys
    
#     def display_info(self):
#         print(f"{self.name} has {self.eye_color} eye colour and {self.toys} toys.")

# p = parent('ram', 'black')
# c = child('seetha', 'brown', 10)

# p.display_info() #ram has black eye colour.
# c.display_info() #seetha has brown eye colour and 10 toys.

# # if child has no display_info
# c.display_info() # seetha has brown eye colour.

# -----------------------------------------------------------
# method overloading

# class parent:
#     def __init__(self, name, eye_color) -> None:
#         self.name = name
#         self.eye_color = eye_color
    
#     def display_info(self):
#         print(f"{self.name} has {self.eye_color} eye colour.")

# class child(parent):
#     def __init__(self, name, eye_color, toys):
#         super().__init__(name, eye_color)
#         self.toys = toys
    
#     def display_info(self):
#         print(f"{self.name} has {self.eye_color} eye colour and {self.toys} toys.")

#     def random(self, a=0, b=None, c=None):
#         if b:
#             return a*b
#         if c:
#             return a+c
#         return a+2

#     # def random(self, a):
#     #     return a*2
#     # def random(self, a, b):
#     #     return a*b
    
# p = parent('ram', 'black')
# c = child('seetha', 'brown', 10)

# # same function, but different no of args
# print(c.random()) #2
# print(c.random(2)) #4
# print(c.random(2, 5)) #10
# print(c.random(2, 5, 6))#10, get into if b:
# print(c.random(2, c=6))#8



# -----------------------------------------------------
# __str__ and __repr__ methods

# class parent:
#     def __init__(self, name, eye_color) -> None:
#         self.name = name
#         self.eye_color = eye_color
    
#     def display_info(self):
#         print(f"{self.name} has {self.eye_color} eye colour.")

#     def __str__(self):
#         return f"{self.name}"
    
#     def __repr__(self):
#         return f"my name is {self.name}"
        
# p = parent('ram', 'black')
# print(p) #ram , will call __str__ function if both functions are present
# ------------------------------------------------------------------

# operator overloading
# using dunder methods: __add__, mul, sub etc

# class parent:
#     def __init__(self, name, pay) -> None:
#         self.name = name
#         self.salary = pay
    
#     def __add__(self, p1):
#         return self.salary + p1.salary
    
#     def __mul__(self, p1):
#         return self.salary * p1.salary
    
#     def __len__(self):
#         return len(''.join(self.name.split(' ')))
    
# p1 = parent('hari', 34000)
# p2 = parent('var', 60000)

# print(len(p1)) #4
# p3 = parent('hari ser', 34000)
# print(len(p3)) #7

# print(p1 + p2)
# print(p1 * p2)

# print(len('varna')) #5
# print('varna'.__len__()) #5

# print(1+2) #3
# print(int.__add__(1, 2)) #3

# print('a'+'b') #ab
# print(str.__add__('a', 'b')) #ab
# print(str.__add__(1, 2)) #err










