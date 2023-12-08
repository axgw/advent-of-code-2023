import unittest
import gear_ratios as day3


class MyTestCase(unittest.TestCase):
    def test_indexes(self):
        s = ".12."
        #     p
        #    0123
        self.assertTrue(day3.get_indexes(s, 1) == (1, 2))
        self.assertTrue(day3.get_indexes(s, 2) == (1, 2))

    def test_number_from_indexes(self):
        s = ".12."
        self.assertTrue(
            day3.get_number_from_indexes(s, 1, 2) == 12)


if __name__ == '__main__':
    unittest.main()
