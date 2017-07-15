import unittest
from main import Vehicle, VehiclePrinter, Engine, EnginePrinter


class TestCars(unittest.TestCase):
    def test_vehicle(self):
        car = Vehicle('Car')
        self.assertEqual(car.name, 'Car')

        car.wheel_count = 4
        self.assertEqual(car.wheel_count, 4)

        car.speed = 30
        self.assertEqual(car.speed, 30)

        car.body_type = 'sedan'
        self.assertEqual(car.body_type, 'sedan')
        self.assertEqual(car.driving_wheels, car.driving_wheels_popular)

        car.body_type = 'jeep'
        self.assertEqual(car.body_type, 'jeep')
        self.assertEqual(car.driving_wheels, car.driving_wheels_jeep)

        car.body_type = 'universal'
        self.assertEqual(car.body_type, 'universal')
        self.assertEqual(car.driving_wheels, '4x2')

        car.drive_unit = 'front'
        self.assertEqual(car.drive_unit, 'front')

        car.gearbox_type = 'A'
        self.assertEqual(car.gearbox_type, 'A')

        car.dimensions = '100x200x50'
        self.assertEqual(car.dimensions, '100x200x50')

        car.tank_volume = '5'
        self.assertEqual(car.tank_volume, '5')

        car._color = 'red'
        self.assertEqual(car.color, 'red')

        car.engine = 'car_engine'
        self.assertEqual(car.engine.name, 'car_engine')

        car_run = car.run('R')
        self.assertEqual(car_run, 'RRRRRRRRRRRRRRRRRRRRRRRRRRRRRR')

        inf = VehiclePrinter()
        # print(VehiclePrinter.print_properties(inf, car))

    def test_engine(self):
        engine = Engine('car_engine')
        self.assertEqual(engine.name, 'car_engine')

        engine.power = 1000
        self.assertEqual(engine.power, 1000)

        engine.engine_capacity = 5
        self.assertEqual(engine.engine_capacity, 5)

        engine.count_cylinders = 4
        self.assertEqual(engine.count_cylinders, 4)

        engine.material = 'steel'
        self.assertEqual(engine.material, 'steel')

        engine.fuel_consumption = 9
        self.assertEqual(engine.fuel_consumption, 9)

        engine.fuel_type = 'gasoline'
        self.assertEqual(engine.fuel_type, 'gasoline')

        engine.oil_consumption = 7
        self.assertEqual(engine.oil_consumption, 7)

        engine.oil_type = 'oil'
        self.assertEqual(engine.oil_type, 'oil')

        inf = EnginePrinter()
        #print(EnginePrinter.print_properties(inf, engine))

if __name__ == '__main__':
    unittest.main()
