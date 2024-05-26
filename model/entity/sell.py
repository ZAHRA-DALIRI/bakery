from model.entity import *

class Sell(Base):
    __tablename__ = "sell_tbl"
    sell_id = Column(Integer, primary_key=True, autoincrement=True)
    date_time= Column(DateTime)
    price = Column(Integer)

    device_id = Column(Integer, ForeignKey("device_tbl.device_id"))
    device = relationship("Device")

    customer_id = Column(Integer, ForeignKey("customer_tbl.customer_id"))
    customer = relationship("Customer")

    emp_id = Column(Integer, ForeignKey("employee_tbl.employee_id"))
    employee = relationship("Employee")


    # todo : init - getter / setter (validation)

