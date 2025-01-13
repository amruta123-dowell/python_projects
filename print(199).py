


# from datetime import date

# class Human:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def description(self):
#         return f'the name is {self.name} and his age is {self.age}'
    
#     @staticmethod
#     def staticmethod(*numbers):
#         return f'sum of the numbers {sum(numbers)}'


#     @classmethod
#     def classmethod(cls, name, dob):
#         currentyear = date.today().year
#         print(currentyear)
#         currentAge = currentyear - dob
#         return cls(name, currentAge)
    

# madhav = Human.classmethod("Madhav", 1998)
# #static method call
# print(Human.staticmethod(20,30))

# #classmethod call
# print(madhav.description())

class Polygon:
    def __init__(self, no_of_sides):
        self.no_of_sides = no_of_sides

    def inputsides(self):
        self.sides= [float(input(f"Enter the side {i+1}")) for i in range(self.no_of_sides)]
        # print(self.sides)
        

    
class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findarea(self):
        a,b,c= self.sides
        print(a, b,c)
        s = (a+b+c)/2
        area = (s-a)*(s-b)*(s-c)*0.5
        print(f"the area is {area}")

t = Triangle()
t.inputsides()
t.findarea()




