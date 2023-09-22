import unittest

from my_sum import sum


class TestSum(unittest.TestCase):

    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    if __name__ == "__main__":
        unittest.main()


"""
The testing showed that the sum function did work when tested using
numbers that add up to 6, and returned an error if the numbers
did not add up to six. Unit testing is good to use when testing small
parts of a program's code. Automated testing is a must for large applications.
"""
