# Fill the Python code in this file
import unittest
from recursive_json_search import *
from test_data import *

class json_search_test(unittest.TestCase):
    '''Test module to test search in `recursive_json_search.py`'''
    def test_search_found(self):
        '''key should be found, list should not be empty'''
        self.assertTrue([] != json_search(key1, data))
    def test_search_not_found(self):
        '''key should not be found, list should be empty'''
        self.assertTrue([] == json_search(key2, data))
    def test_is_a_list(self):
        '''should return a list'''
        self.assertIsInstance(json_search(key1, data), list)

if __name__ == '__main__':
    unittest.main()