import unittest

class ClusterTest(unittest.TestCase):
    def test_basic(self):
        pass


def suite():
    tests = ['test_basic']
    return unittest.TestSuite(map(ClusterTest, tests))

