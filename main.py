class Vehicle(object):
    def __init__(self, name):
        self.name = name

    sedan = 'sedan'
    jeep = 'jeep'
    driving_wheels_popular = '4x2'
    driving_wheels_jeep = '4x4'

    @property
    def _wheel_count(self):
        return self.wheel_count

    @_wheel_count.setter
    def _wheel_count(self, value):
        self.wheel_count = value

    @property
    def _speed(self):
        print(self.speed)

    @_speed.setter
    def _speed(self, value):
        self.speed = value

    @property
    def _body_type(self):
        print(self.body_type)

    @_body_type.setter
    def _body_type(self, value):
        self.body_type = value

    @property
    def _driving_wheels(self):
        print(self.driving_wheels)

    @_driving_wheels.setter
    def _driving_wheels(self, value):
        print(self.body_type)
        print(self.sedan)
        if self.body_type == self.sedan:
            self.driving_wheels = self.driving_wheels_popular
        elif self.body_type == self.jeep:
            self.driving_wheels = self.driving_wheels_jeep
        else:
            self.driving_wheels = value

    @property
    def _drive_unit(self):
        print(self.drive_unit)

    @_drive_unit.setter
    def _drive_unit(self, value):
        self.drive_unit = value

    @property
    def _gearbox_type(self):
        print(self.gearbox_type)

    @_gearbox_type.setter
    def _gearbox_type(self, value):
        self.gearbox_type = value

    @property
    def _dimensions(self):
        print(self.dimensions)

    @_dimensions.setter
    def _dimensions(self, value):
        self.dimensions = value

    @property
    def _tank_volume(self):
        print(self.volumetank)

    @_tank_volume.setter
    def _tank_volume(self, value):
        self.tank_volume = value

    @property
    def _color(self):
        print(self.color)

    @_color.setter
    def _color(self, value):
        self.color = value

    @property
    def _engine(self):
        print(self.engine)

    @_engine.setter
    def _engine(self, value):
        self.engine = Engine(value)

    def beep(self):
        pass

    def run(self):
        s = 1
        while s < self.speed:
            print('R', end='')
            s += 1

class VehiclePrinter():
    def Printer(self, vehicle):
        print('название: ', format(vehicle.name))
        print('количество колес: ', format(vehicle.wheel_count))
        print('скорость: ', format(vehicle.speed))
        print('тип кузова: ', format(vehicle.body_type))
        print('привод: ', format(vehicle.privod))
        print('КП: ', format(vehicle.typekp))
        print('габариты: ', format(vehicle.dimensions))
        print('объем бака: ', format(vehicle.volumetank))
        print('двигатель: ', format(vehicle.engine.name))


class Engine:
    def __init__(self, name):
        self.name = name

    def createproperties(self, power, volume, countcylindr,
                         material, fuelconsump, typefuel,
                         oilconsump, typeoil):
        self.power = power
        self.volume = volume
        self.countcylindr = countcylindr
        self.material = material
        self.fuelconsump = fuelconsump
        self.typefuel = typefuel
        self.oilconsump = oilconsump
        self.typeoil = typeoil

    def turnOn(self):
        pass

    def turnOff(self):
        pass

    def info(self):
        print('мощность: ', format(self.power))
        print('объем: ', format(self.volume))
        print('количество цилиндров: ', format(self.countcylindr))
        print('материал: ', format(self.material))
        print('расход топлива: ', format(self.fuelconsump))
        print('тип топлива: ', format(self.typefuel))
        print('расход масла: ', format(self.oilconsump))
        print('тип масла: ', format(self.typeoil))


class EnginePrinter:
    def printer(self, engine):
        print('мощность: ', format(engine.power))
        # todo

car = Vehicle('car')
car.body_type = 'sedan'
car.driving_wheels = '2'
print(car.body_type == car.sedan)
print(car.body_type)
print(car.sedan)
print(car.driving_wheels)