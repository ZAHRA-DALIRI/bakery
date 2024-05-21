from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from bakery.model.entity.base import Base
from bakery.model.entity.device_components import Component


class Device(Base):
    __tablename__ = "device_tbl"
    device_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    model = Column(String(20), nullable=False)

    components = relationship(Component)

    def __init__(self, device_id, name, model):
        self.device_id = device_id
        self.name = name
        self.model = model
