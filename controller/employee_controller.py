from model.bl.employee_bl import EmployeeBl
from model.entity.employee import Employee
from model.tools.decorators import exception_handling


class EmployeeController:
    @staticmethod
    @exception_handling
    def save(id, name, family, national_code, phone_number, email, address,
             birth_certificate, birth_date, field_of_study, grade, average, start_date,
             completion_date, university_name, status):
        employee = Employee(id, name, family, national_code, phone_number, email, address,
                            birth_certificate, birth_date, field_of_study, grade, average, start_date,
                            completion_date, university_name, status)
        return True, EmployeeBl.save(employee)

    @staticmethod
    @exception_handling
    def edit(id, name, family, national_code, phone_number, email, address,
             birth_certificate, birth_date, field_of_study, grade, average, start_date,
             completion_date, university_name, status=True):
        employee = Employee(id, name, family, national_code, phone_number, email, address,
                            birth_certificate, birth_date, field_of_study, grade, average, start_date,
                            completion_date, university_name, status)
        return True, EmployeeBl.edit(employee)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, EmployeeBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, EmployeeBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, EmployeeBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_family(family):
        return True, EmployeeBl.find_by_family(family)
