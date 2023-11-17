class Employee:
    emp_list = []
    
    def __init__(self, name, id, salary, dept):
        self.name = name
        self.id = id
        self.salary = salary
        self.dept = dept
        self.emp_list.append(self)
    
    def assignDepartment(self, new_dept):
        self.dept = new_dept
    
    def printInfo(self):
        print(f"\nname: {self.name}\nemp id: {self.id}\
            \nsalary: {self.salary}\ndepartment: {self.dept}\n----------------------------")
    
    def calculateSalary(self, salary, hrs):
        overtime = 0

        if hrs > 50:
            overtime = hrs - 50
        
        self.salary = self.salary + (overtime * (salary / 50))

emp1 = Employee("ADAMS", "E7876", 50000, "ACCOUNTING")
emp2 = Employee("JONES", "E7499", 45000, "RESEARCH")
emp3 = Employee("MARTIN", "E7900", 50000, "SALES")
emp4 = Employee("SMITH", "E7698", 55000, "OPERATIONS")

for each in Employee.emp_list:
    each.printInfo()

emp2.assignDepartment("ADMINISTRATIONS")

emp3.calculateSalary(45000, 45)
emp3.calculateSalary(45000, 50)
emp3.calculateSalary(45000, 52)
emp4.calculateSalary(45000, 60)

# print updated employee list
for each in Employee.emp_list:
    each.printInfo()