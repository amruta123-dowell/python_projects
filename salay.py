# Salary composition
class Salary:
    def __init__(self, salary, bonus):
        self.salary = salary*12
        self.bonus = bonus

    def calculateSalary(self):
        return (self.salary+self.bonus)
    
class Employee:
    def __init__(self, empName, salary, age, bonus):
        self.empName = empName
        self.salary = salary
        self.age = age
        self.total_salary = Salary(salary=salary, bonus=bonus)

    def empdetails(self):
        return f'the name is {self.empName} , age is {self.age}. he got total money {self.total_salary.calculateSalary()}'

empDetails = Employee("amruta",  50000,23, 20000)
print(empDetails.empdetails())