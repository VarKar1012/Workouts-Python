from abc import ABC, abstractmethod

class vehicle(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def change_gear(self):
        print("gear change")

class car(vehicle):
    def change_gear(self):
        print("changing gear of car")

class truck(vehicle):
    def change_gear(self):
        print("changing gear of truck")

c = car()
t = truck()

c.change_gear()
t.change_gear()
# changing gear of car
# changing gear of truck

v = vehicle() #=> can't instantiate abstract class
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Traceback (most recent call last):
#   File "d:\ExpertzLab\PythonSamples\prog\abstraction.py", line 27, in <module>
#     v = vehicle()
#         ^^^^^^^^^
# TypeError: Can't instantiate abstract class vehicle with abstract method change_gear