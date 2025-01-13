#user defined module
import file_one


#built in module 
import datetime 

#You can use "from" keyword to import specific method from module
# eg: from datetime import datetime
# from file_one import add

def sumvalue():
    return file_one.add(20,30)

def multiply():
    return file_one.multi(2,3)

def printTodayDate():
    return f'Today date is {datetime.datetime.today()}'

print(sumvalue())
print(multiply())
print(printTodayDate())

#to get the methods defined in imported module
print(f"datetime module contains --------> {dir(datetime)}")
print(f"file_one module contains {dir(file_one)}")