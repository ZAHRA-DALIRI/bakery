from sqlalchemy import Column, Integer, String, Boolean, DateTime

from bakery.model.entity.base import Base


class Employee(Base):
    __tablename__ = "employee_tbl"
    employee_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    national_code = Column(Integer, unique=True, nullable=True)
    phone_number = Column(Integer, nullable=True)
    email = Column(String(20), nullable=False)
    address = Column(String(40), nullable=False)
    birth_certificate = Column(String(20), unique=True, nullable=True)
    birth_date = Column(DateTime, nullable=True)
    field_of_study = Column(String(20), nullable=True)
    grade = Column(String(20), nullable=True)
    average = Column(Integer, nullable=True)
    start_date = Column(DateTime, nullable=True)
    completion_date = Column(DateTime, nullable=True)
    university_name = Column(String(20), nullable=True)
    status = Column(Boolean, default=True)

    def __init__(self, employee_id, name, family, national_code, phone_number, email, address,
                 birth_certificate, birth_date, field_of_study, grade, average, start_date,
                 completion_date, university_name, status=True):
        self.employee_id = employee_id
        self.name = name
        self.family = family
        self.national_code = national_code
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.birth_certificate = birth_certificate
        self.birth_date = birth_date
        self.field_of_study = field_of_study
        self.grade = grade
        self.average = average
        self.start_date = start_date
        self.completion_date = completion_date
        self.university_name = university_name
        self.status = status
