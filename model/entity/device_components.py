from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from bakery.model.entity.device import Device
from bakery.model.entity.base import Base


class Component(Base):
    __tablename__ = "component_tbl"
    component_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)
    serial = Column(String(20), nullable=False)
    description = Column(String(100))

    device_id = Column(Integer, ForeignKey("device_tbl.device_id"))
    device = relationship(Device)

    def __init__(self, Component_id, name, model, serial, description, device):
        self.Component_id = Component_id
        self.name = name
        self.model = model
        self.serial = serial
        self.description = description
        self.device = device
