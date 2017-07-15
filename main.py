class Vehicle(object):
    def __init__(self, name):
        self.name = name
        self._wheel_count = 0
        self._speed = 0
        self._body_type = ''
        self._driving_wheels = ''
        self._drive_unit = ''
        self._gearbox_type = ''
        self._dimensions = ''
        self._tank_volume = ''
        self._color = ''
        # self._engine = ''

    sedan = 'sedan'
    jeep = 'jeep'
    driving_wheels_popular = '4x2'
    driving_wheels_jeep = '4x4'
    driving_wheels_base = 'x2'

    @property
    def wheel_count(self):
        return self._wheel_count

    @wheel_count.setter
    def wheel_count(self, value):
        self._wheel_count = value

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def body_type(self):
        return self._body_type

    @body_type.setter
    def body_type(self, value):
        self._body_type = value
        if self._body_type == self.sedan:
            self._driving_wheels = self.driving_wheels_popular
        elif self._body_type == self.jeep:
            self._driving_wheels = self.driving_wheels_jeep
        else:
            self._driving_wheels = str(self._wheel_count) + self.driving_wheels_base

    @property
    def driving_wheels(self):
        return self._driving_wheels

    @property
    def drive_unit(self):

        return self._drive_unit

    @drive_unit.setter
    def drive_unit(self, value):
        self._drive_unit = value

    @property
    def gearbox_type(self):
        return self._gearbox_type

    @gearbox_type.setter
    def gearbox_type(self, value):
        self._gearbox_type = value

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        self._dimensions = value

    @property
    def tank_volume(self):
        return self._tank_volume

    @tank_volume.setter
    def tank_volume(self, value):
        self._tank_volume = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        self._color = value

    @property
    def engine(self):
        return self._engine

    @engine.setter
    def engine(self, value):
        self._engine = Engine(value)

    def beep(self):
        pass

    def run(self, letter):
        s = 0
        run_value = ''
        while s < self.speed:
            run_value = run_value + letter
            s += 1
        return run_value


class VehiclePrinter:
    def print_properties(self, vehicle):
        print('название: ', format(vehicle.name))
        print('количество колес: ', format(vehicle.wheel_count))
        print('скорость: ', format(vehicle.speed))
        print('тип кузова: ', format(vehicle.body_type))
        print('Веудущие колеса: ', format(vehicle.driving_wheels))
        print('тип кузова: ', format(vehicle.drive_unit))
        print('КП: ', format(vehicle.gearbox_type))
        print('габариты: ', format(vehicle.dimensions))
        print('объем бака: ', format(vehicle.tank_volume))
        print('цвет: ', format(vehicle.color))
        print('двигатель: ', format(vehicle.engine.name))


class Engine:
    def __init__(self, name):
        self.name = name
        self._power = 0
        self._engine_capacity = 0
        self._count_cylinders = 0
        self._material = ''
        self._fuel_consumption = 0
        self._fuel_type = ''
        self._oil_consumption = 0
        self._oil_type = ''

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def engine_capacity(self):
        return self._engine_capacity

    @engine_capacity.setter
    def engine_capacity(self, value):
        self._engine_capacity = value

    @property
    def count_cylinders(self):
        return self._count_cylinders

    @count_cylinders.setter
    def count_cylinders(self, value):
        self._count_cylinders = value

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, value):
        self._material = value

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self._fuel_consumption = value

    @property
    def fuel_type(self):
        return self._fuel_type

    @fuel_type.setter
    def fuel_type(self, value):
        self._fuel_type = value

    @property
    def oil_consumption(self):
        return self._oil_consumption

    @oil_consumption.setter
    def oil_consumption(self, value):
        self._oil_consumption = value

    @property
    def oil_type(self):
        return self._oil_type

    @oil_type.setter
    def oil_type(self, value):
        self._oil_type = value

    def turnOn(self):
        pass

    def turnOff(self):
        pass

class EnginePrinter:
    def print_properties(self, engine):
        print('мощность: ', format(engine.power))
        print('объем: ', format(engine.engine_capacity))
        print('количество цилиндров: ', format(engine.count_cylinders))
        print('материал: ', format(engine.material))
        print('расход топлива: ', format(engine.fuel_consumption))
        print('тип топлива: ', format(engine.fuel_type))
        print('расход масла: ', format(engine.oil_consumption))
        print('тип масла: ', format(engine.oil_type))
