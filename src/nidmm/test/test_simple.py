
import unittest
import nidmm
print("import nidmm")

class SimpleUnitTest(unittest.TestCase):
    '''
    Simple unit test that just makes sure the created package in import-able
    '''

    def test_simple(self):
        assert True
