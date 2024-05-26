from datetime import datetime

from model.da.da import DataAccess
from model.entity import *
from model.entity.sell import Sell

customer =  Customer()
customer.name = "ali"
customer.family = "alipour"
c_da  = DataAccess(Customer)
c_da.save(customer)
customer = c_da.find_by_id(1)
print(customer)

employee = Employee()
employee.name = "reza"
employee.family = "rezaii"
e_da = DataAccess(Employee)
e_da.save(employee)
employee = e_da.find_by_id(1)
print(employee)

device = Device()
device.name = "bakery a1000"
d_da = DataAccess(Device)
d_da.save(device)
device = d_da.find_by_id(1)
print(device)

comp1 = Component()
comp1.name = "ic1"
comp1.device = device

comp2 = Component()
comp2.name = "ic1"
comp2.device = device

co_da = DataAccess(Component)
co_da.save(comp1)
print(comp2)
co_da.save(comp2)
print(comp2)

d = d_da.find_by(Device.name == "bakery a1000")
print("DEVICE ",d)
print("COMP :", d[0].components)

sell = Sell()
sell.customer = customer
sell.employee = employee
sell.date = datetime.now()
sell.price = 1000
sell.device=  device

sell_da = DataAccess(Sell)
sells = sell_da.save(sell)

print(sell_da.find_all())








# from controller.person_controller import PersonController

# print(PersonController.save("ahmad", "messbah"))
# print(PersonController.edit(1, "ali", "messbah"))
# print(PersonController.remove(1))
# print(PersonController.find_all())
# print(PersonController.find_by_id(10))
# print(PersonController.find_by_family("messbah1"))


# print(PersonController.edit(1, "ali", "messbah"))


