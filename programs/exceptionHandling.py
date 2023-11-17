# try, except, finally blocks

# try: #code that might throw an error
#     num1 = 10
#     num2 = 0 #5
#     out = num1 / num2
#     print(out)
# except: #executes when an err occurs
#     print("Division by zero err occured. Please change the value of num2")
# finally: #code that always executes regardless of the exception or not.
#     print("program is running")

# print("completed")
# output---
# nums = 10, 5
# 2.0
# program is running
# completed

# nums = 10, 0
# Division by zero err occured. Please change the value of num2
# program is running
# completed


# num1 = 10
# num2 = 0
# try:
#     out = num1 / num2 
# except ZeroDivisionError:
#     print("Division by zero occured. Please check the divisor.")
# except NameError:
#     print("please check for an undefined variable.")
# except:
#     print("Check you code for errors.")
# # Division by zero occured. Please check the divisor.


# num1 = 10
# num2 = 0
# try:
#     print(val)
#     out = num1 / num2 
# except ZeroDivisionError:
#     print("Division by zero occured. Please check the divisor.")
# except NameError:
#     print("please check for an undefined variable.")
# except:
#     print("Check you code for errors.")
# # please check for an undefined variable.

l = ['val', 2, 0, 5]
for i in l:
    try:
        print(i / 1)
    except:
        pass

print("completed")
# output - Here, str var is not detected as err but at the same time, list is traversed 
# 2.0
# 0.0
# 5.0
# completed










