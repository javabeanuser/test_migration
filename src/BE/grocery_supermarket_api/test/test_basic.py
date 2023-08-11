import unittest


class BasicTestSuite(unittest.TestCase):
    def test_absolute_truth(self):
        assert True

if __name__ == '__main__':
    unittest.main()