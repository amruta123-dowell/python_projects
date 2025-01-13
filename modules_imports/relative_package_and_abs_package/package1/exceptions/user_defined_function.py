class InvalidException(Exception):
    pass

class CustomException(Exception):
    def __init__(self, age, message ="You are not eligible for voting"):
        self.age=age
        self.message= message
        super().__init__(self.message)
try:
    age = int(input("How old you are? "))
    if age<18 :
        # raise InvalidException()
        raise CustomException(age)
    else:
        print("valid age for voting")
except InvalidException:
    print("Invalid age to vote")
