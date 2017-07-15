import unittest
from main import Vehicle


class TestCars(unittest.TestCase):
    def test_vehicle(self):
        car = Vehicle('Car')
        self.assertEqual(car.name, 'Car')

        car.wheels_count = 4
        self.assertEqual(car.wheels_count, 4)

        car.speed = 200
        self.assertEqual(car.speed, 200)

        car.body_type = 'sedan'
        self.assertEqual(car.body_type, 'sedan')

        car.driving_wheels = '4x0'
        print(car.body_type == car.sedan)
        self.assertEqual(car.driving_wheels, car.driving_wheels_popular)

        car.drive_unit = 'front'
        self.assertEqual(car.drive_unit, 'front')

        car.gearbox_type = 'A'
        self.assertEqual(car.gearbox_type, 'A')

        car.dimensions = '100x200x50'
        self.assertEqual(car.dimensions, '100x200x50')

        car.tank_volume = '5'
        self.assertEqual(car.tank_volume, '5')

        # def test_engine(self):
        #    self.assertTrue('FOO'.isupper())
        #    self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()
