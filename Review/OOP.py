# class Employee(object):
#
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
#
#     def set_salary(self, salary):
#         self.__salary = salary
#
#     def get_salary(self):
#         return self.__salary
#
#     salary = property(get_salary, set_salary)
#
#
# Albert = Employee('Albert', 6000)
# print(Albert.salary)
#
#
# class Blood_Pressure(object):
#
#     def __init__(self, name, age, lp=70, hp=80):
#         self.name = name
#         self.age = age
#         self.__lp = lp
#         self.__hp = hp
#
#     def set_lp_pressure(self, lp):
#         self.__lp = lp
#
#     def set_hp_pressure(self, hp):
#         self.__hp = hp
#
#     def get_hp_pressure(self):
#         return self.__hp
#
#     def get_lp_pressure(self):
#         return self.__lp
#
#     lp = property(get_lp_pressure, set_lp_pressure)
#     hp = property(get_hp_pressure, set_hp_pressure)
#
#
# saribeg = Blood_Pressure('saribeg', 27, 50, 88)
# print(saribeg.hp)
# print(saribeg.lp)

# class Vehicle(object):
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def show(self):
#         print("Vehicle Name: {} Speed: {} Mileage: {}".format(self.name, self.max_speed, self.mileage))
#
#
# modelX = Vehicle("ferrari", 240, 18)
# modelX.show()
# class Vehicle:
#     pass
#
#
# class Bus(Vehicle):
#     pass
#
#
# volvo = Bus("Volvo", 240, 18)
# volvo.show()
# class Vehicle(object):
#     color = "White"
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
#
# class Bus(Vehicle):
#     def seating_capacity(self, capacity=50):
#         return super(Bus, self).seating_capacity(capacity=capacity)
#
#
# volvo = Bus("Volvo", 240, 18)
# print(volvo.seating_capacity())
# print(volvo.color)
# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#
#     def fare(self):
#         return self.capacity * 100
#
#
# class Bus(Vehicle):
#     def fare(self):
#         final_amount = super().fare() * 10//100 + super(Bus, self).fare()
#         return final_amount
#
#
# school_BUs = Bus("volvo", 20, 50)
# print(school_BUs.fare())

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity


class Bus(Vehicle):
    pass


School_bus = Bus("School Volvo", 12, 50)
print(School_bus.__class__)
print(School_bus.__dir__())
print(type(School_bus))
print(isinstance(School_bus, Vehicle))
print(issubclass(Bus, Vehicle))