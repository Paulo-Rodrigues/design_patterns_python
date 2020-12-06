from unittest import main, TestCase
from factory_method import CoordinateSystem, Point

class TestPoint(TestCase):
    def test_new_cartesian_point(self):
        point = Point.new_cartesian_point(2,3)
        self.assertIsInstance(point, Point)

    def test_new_cartesian_point(self):
        point = Point.new_cartesian_point(2,3)
        self.assertEqual(point.x, 2)
        self.assertEqual(point.y, 3)

    def test_new_polar_point(self):
        point = Point.new_polor_point(2,3)
        self.assertIsInstance(point, Point)

    def test_new_polar_point(self):
        point = Point.new_polor_point(2,3)
        self.assertEqual(round(point.x, 2), -1.98)
        self.assertEqual(round(point.y, 2), 0.28)

if __name__=='__main__':
    main()
