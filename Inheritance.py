# 1. Single Inheritance
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person): 
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

# 2. Multiple Inheritance
class Job:
    def __init__(self, salary):
        self.salary = salary

class EmployeePersonJob(Employee, Job):  
    def __init__(self, name, salary):
        Employee.__init__(self, name, salary) 
        Job.__init__(self, salary)           

# 3. Multilevel Inheritance
class Manager(EmployeePersonJob):
    def __init__(self, name, salary, department):
        EmployeePersonJob.__init__(self, name, salary)  
        self.department = department

# Single Inheritance
emp = Employee("malar", 40000)
print(emp.name, emp.salary)

# Multiple Inheritance
emp2 = EmployeePersonJob("sharmi", 50000)
print(emp2.name, emp2.salary)

# Multilevel Inheritance
mgr = Manager("viji", 60000, "ASE")
print(mgr.name, mgr.salary, mgr.department)

