num1= 2
num2 =0

list = [20,40]

try:
    # print(num1/num2)
    print(list[9])

except IndexError as e:
    print("The index error is ", e)

except ZeroDivisionError as e:
    print("The division error is ", e)

except Exception as e:
    print("The exception is", e)

else:
    print("I am different error")

finally:
    print("The code is executed")