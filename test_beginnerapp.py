import unittest
from beginnerapp import csv_to_json_convertor
import os


class TestType(unittest.TestCase):

    def setting_up(self):
        self.sh = csv_to_json_convertor()
        print(self.sh)

    def test_processed_output_exist(self):
        """To test if the output Json file exist after running the main file."""
        self.assertTrue(os.path.exists('./struct.json'))

    def test_output_exsist(self):
        """Check if the output file is attached"""
        self.assertTrue(os.path.exists('./output.txt'))


    # def test_dict(self):
    #     message = 'This is to check function value is not none'
    #     self.assertIsNotNone(self.sh, message)

    def test_assert_is_instance(self):
        """This method is to check that the output type or class of the code is in dictionary form."""
        self.test_assert_is_instance(self.sh, dict)

    # def test_assert_count_equal(self):
    #     self.assertCountEqual(self.fm['link'], 'https://groceries.morrisons.com/browse/178974')

if __name__ == '__main__':
    unittest.main()



