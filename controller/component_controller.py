from model.bl.component_bl import ComponentBl
from model.entity.device_components import Component
from model.tools.decorators import exception_handling


class ComponentController:
    @staticmethod
    @exception_handling
    def save(id, name, model, serial, description):
        component = Component(id, name, model, serial, description)
        return True, ComponentBl.save(component)

    @staticmethod
    @exception_handling
    def edit(name, model, serial, description):
        component = Component(name, model, serial, description)
        return True, ComponentBl.edit(component)

    @staticmethod
    @exception_handling
    def remove(id):
        return True, ComponentBl.remove(id)

    @staticmethod
    @exception_handling
    def find_all():
        return True, ComponentBl.find_all()

    @staticmethod
    @exception_handling
    def find_by_id(id):
        return True, ComponentBl.find_by_id(id)

    @staticmethod
    @exception_handling
    def find_by_serial(serial):
        return True, ComponentBl.find_by_serial(serial)
