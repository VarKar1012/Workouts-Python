# use private variables and methods

# class car:
#     def __init__(self) -> None:
#         self.update()

#     def update(self):
#         print("updating")

#     def drive(self):
#         print("driving")

# a = car()
# a.drive()
# updating
# driving
# ---------------------------------
# after encapsulation - creating private vars/methods using __ as prefix

# class car:
#     def __init__(self) -> None:
#         self.__update()

#     def __update(self):
#         print("updating")

#     def drive(self):
#         print("driving")

# a = car()
# a.drive()
# a.__update()
# updating
# driving
# Traceback (most recent call last):
#   File "d:\ExpertzLab\PythonSamples\prog\encapsulation.py", line 32, in <module>
#     a.__update()
#     ^^^^^^^^^^
# AttributeError: 'car' object has no attribute '__update'
# -------------------------------------------------------------
# class car:
#     def __init__(self) -> None:
#         self.__update()

#     def __update(self):
#         print("updating")

#     def drive(self):
#         print("driving")

# a = car()
# a.drive()
# updating
# driving
# private members can't be accessed outside of the class or inside the child class.
# it can only be accessed from inside the methods of that class.


# class car:
#     # var = __update => err can't 

#     def __init__(self) -> None:
#         self.__update()

#     def __update(self):
#         print("updating")

#     def drive(self):
#         print("driving")

# a = car()
# a.drive()

# -----------------------------------------------------------------
# encapsulation - private vars

class car:
    __maxSpeed = 200

    def __init__(self) -> None:
        print("max speed:", self.__maxSpeed)

    def __update(self):
        print("updating")

    def drive(self):
        print("driving...& max speed is", self.__maxSpeed)

    def setSpeed(self, speed):
        self.__maxSpeed = speed

a = car()
a.drive()
# # max speed: 200
# # driving...& max speed is 200

a.setSpeed(300)
a.drive()
# driving...& max speed is 300

print(a.__dict__)
# {'_car__maxSpeed': 300}

car.__maxSpeed = 400 # no  err, but wont set to private var
print(a.__dict__)
# {'_car__maxSpeed': 300}

# calling private method returns err