from controller.exceptions.exceptoins import DeviceNotFoundError
from model.da.da import DataAccess
from model.entity import Device

Device_da = DataAccess(Device)


class DeviceBl:
    @staticmethod
    def save(device_id, name, model):
        return Device_da.save(device_id, name, model)

    @staticmethod
    def edit(device_id,):
        if Device_da.find_by_id(device_id):
            return Device_da.edit(Device)
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def remove(id):
        Device = Device_da.find_by_id(id)
        if Device:
            return Device_da.remove(Device)
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def find_all():
        Device_list = Device_da.find_all()
        if Device_list:
            return Device_list
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def find_by_id(id):
        Device = Device_da.find_by_id(id)
        if Device:
            return Device
        else:
            raise DeviceNotFoundError()

    @staticmethod
    def find_by_model(model):
        Device_list = Device_da.find_by(Device.model == model)
        if Device_list:
            return Device_list
        else:
            raise DeviceNotFoundError()

