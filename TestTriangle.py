# -*- coding: utf-8 -*-
"""
Updated Sept 17, 2022
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
@author : hrehman
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(201, 202, 203), 'InvalidInput', '201, 202, 203 should return InvalidInput')
    
    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(-1, -4, -5), 'InvalidInput', '-1, -4, -5 should return InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle('foo', 'bar', 'baz'), 'InvalidInput', 'foo, bar, baz should return InvalidInput')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1, 1, 2), 'NotATriangle', '1, 1, 2 is NotATriangle')
    
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(7, 12, 15), 'Scalene', '7, 12, 15 should be a Scalene Triangle')
    
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(4, 4, 6), 'Isosceles', '4, 4, 6 is an Isosceles Triangle')

    def testEquilateralWithDecimals(self):
        self.assertEqual(classifyTriangle(6.5, 6.5, 6.5), 'Equilateral', '6.5, 6.5, 6.5 is an Equilateral Triangle')
    
    def testIsoscelesTriangleWithDecimals(self):
        self.assertEqual(classifyTriangle(4.6, 4.6, 6.9), 'Isosceles', '4.6, 4.6, 6.9 is an Isosceles Triangle')
    
    def testRightTriangleWithDecimals(self):
        self.assertEqual(classifyTriangle(6, 8, 10.00000001), 'Right', '6, 8, 10 is a Right Triangle')

    def testScaleneTriangleWithDecimals(self):
        self.assertEqual(classifyTriangle(12.5, 7.5, 15.5), 'Scalene', '7.5, 12.5, 15.5 is a Scalene Triangle')
        

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

