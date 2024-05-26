from model.bl.device_bl import DeviceBl
from model.entity.device import Device
from model.tools.decorators import exception_handling


class DeviceController:
    @staticmethod
    @exception_handling
    def save(id, name, model):
        device = Device(id, name, model)
        return True, DeviceBl.save(device)

    @staticmethod
    @exception_handling
    def edit(name, model):
        device = Device(name, model)
        return True, DeviceBl.edit(device)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, DeviceBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, DeviceBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, DeviceBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_model(model):
        return True, DeviceBl.find_by_model(model)
