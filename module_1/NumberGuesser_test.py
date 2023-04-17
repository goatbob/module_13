
import unittest
from NumberGuesser_class import n as n


class NumberGuesserTest(unittest.TestCase):

    def setUp(self):  # set up class
        self.num = n(5)

    def tearDown(self):  # tear down class
        del self.num

    def test_object_created_required_attributes(self):  # test required attributes for class
        self.assertEqual(self.num.random_number, 5)

    def test_get_number_function(self):
        self.assertEqual(self.num.get_number_list(), [])

    def test_get_number_function_2(self):
        n.guessed_list = [1, 2, 3, 4, 5]
        self.assertEqual(self.num.get_number_list(), [1, 2, 3, 4, 5])

    def test_add_number_function(self):
        n.guessed_list = [2, 3, 4, 5]
        self.assertEqual(self.num.add_number(1), [2, 3, 4, 5, 1])


if __name__ == '__main__':
    unittest.main()
