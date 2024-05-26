from model.bl.customer_bl import CustomerBl
from model.entity.customer import Customer
from model.tools.decorators import exception_handling


class CustomerController:
    @staticmethod
    @exception_handling
    def save(id, name, family, national_code, phone_number, email, address, birth_date, status):
        customer = Customer(id, name, family, national_code, phone_number, email, address, birth_date, status)
        return True, CustomerBl.save(customer)

    @staticmethod
    @exception_handling
    def edit(name, family, national_code, phone_number, email, address, birth_date, status=True):
        customer = Customer(name, family, national_code, phone_number, email, address, birth_date, status)
        return True, CustomerBl.edit(customer)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, CustomerBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, CustomerBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, CustomerBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, CustomerBl.find_by_family(family)
