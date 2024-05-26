from model.entity import *



class Device(Base):
    __tablename__ = "device_tbl"
    device_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=True)

    components = relationship("Component", back_populates="device")

    # def __init__(self, device_id, name, model):
    #     self.device_id = device_id
    #     self.name = name
    #     self.model = model

    # todo : getter / setter (validation)