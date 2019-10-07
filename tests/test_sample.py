"""
A micro-service passing back enhanced information from Astronomy
Picture of the Day (APOD).

Adapted from code in https://github.com/nasa/planetary-api

Created on August 8, 2019

@author=samyanez94 @email=samuelyanez94@gmail.com
"""

import unittest

class TestSample(unittest.TestCase):

    def test_sample(self):
        self.assertNotEqual("Lion", "Giraffe")

if __name__ == '__main__':
    unittest.main()
