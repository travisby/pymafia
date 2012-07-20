import unittest


class MyFuncTestCase(unittest.TestCase):
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEqual((a, 0), 'larry')
        self.assertEqual((a, 1), 'curly')
