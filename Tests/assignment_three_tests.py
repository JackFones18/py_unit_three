# Jack Fones
# 10-16-2023


import unittest
import assignment_three

'''
class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here
'''


# I tried using https://docs.python.org/3/library/unittest.html to help me with the unit tests but im still not
# entirely sure why it's not working.
class TestFunctions(unittest.TestCase):
    def test_get_side_length(self):
        with unittest.mock.patch('builtins.input', return_value="3.5"):
            self.assertTrue(type(assignment_three.get_side_length() == float))

    def test_get_color(self):
        with unittest.mock.patch('builtins.input', return_value="red"):
            self.assertTrue(type(assignment_three.get_color() == str))


if __name__ == '__main__':
    unittest.main()
