from model.entity import *


class Customer(Base):
    __tablename__ = "customer_tbl"
    customer_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    family = Column(String(20), nullable=False)
    national_code = Column(String(10), unique=True, nullable=True)
    phone_number = Column(Integer, nullable=True)
    email = Column(String(50), nullable=True)
    address = Column(String(100), nullable=True)
    birth_date = Column(Date, nullable=True)
    status = Column(Boolean, default=True)

    sells = relationship("Sell", back_populates="customer")

    # def __init__(self, customer_id, name, family, national_code, phone_number, email, address, birth_date, status=True):
    #     self.customer_id = customer_id
    #     self.name = name
    #     self.family = family
    #     self.national_code = national_code
    #     self.phone_number = phone_number
    #     self.email = email
    #     self.address = address
    #     self.birth_date = birth_date
    #     self.status = status

    # todo : getter / setter (validation)


