### Assignment 2a

@author: hrehman

Assignment 2a : Testing a Legacy Program and reporting on testing results

#### Part 1

| Test ID | Input | Expected Results | Actual Results | Pass or Fail |
| ------- | ----- | ---------------- | -------------- | ------------ |
|  testRightTriangleA | 3, 4, 5 | Right | InvalidInput | Fail |
| testRightTriangleB | 5, 3, 4 | Right | InvalidInput | Fail |
| testEquilateralTriangles | 1, 1, 1 | Equilateral | InvalidInput | Fail |
| testInvalidInputA | 201, 202, 203 | InvalidInput | InvalidInput | Pass |
| testInvalidInputB | -1, -4, -5 | InvalidInput | InvalidInput | Pass |
| testInvalidInputC | foo, bar, baz | InvalidInput | ERROR | Fail |
| testNotATriangle | 1, 1, 2 | NotATriangle | InvalidInput | Fail |
| testScaleneTriangle | 7, 12, 15 | Scalene | InvalidInput | Fail |
| testIsoscelesTriangle | 4, 4, 6 | Isosceles | InvalidInput | Fail |

#### Part 2

| Test ID | Input | Expected Results | Actual Results | Pass or Fail |
| ------- | ----- | ---------------- | -------------- | ------------ |
|  testRightTriangleA | 3, 4, 5 | Right | Right | Pass |
| testRightTriangleB | 5, 3, 4 | Right | Right | Pass |
| testEquilateralTriangles | 1, 1, 1 | Equilateral | Equilateral | Pass |
| testInvalidInputA | 201, 202, 203 | InvalidInput | InvalidInput | Pass |
| testInvalidInputB | -1, -4, -5 | InvalidInput | InvalidInput | Pass |
| testInvalidInputC | foo, bar, baz | InvalidInput | InvalidInput | Pass |
| testNotATriangle | 1, 1, 2 | NotATriangle | NotATriangle | Pass |
| testScaleneTriangle | 7, 12, 15 | Scalene | Scalene | Pass |
| testIsoscelesTriangle | 4, 4, 6 | Isosceles | Isosceles | Pass |
| testEquilateralTriangleWithDecimals | 6.5, 6.5, 6.5 | Equilateral | Equilateral | Pass |
| testIsoscelesTriangleWithDecimals | 4.6, 4.6, 6.9 | Isosceles | Isosceles | Pass |
| testRightTriangleWithDecimals | 6, 8, 10.000001 | Right | Right | Pass |
| testScaleneTriangleWithDecimals | 12.5, 7.5, 15.5 | Scalene | Scalene | Pass |

#### Assignment Summary

| - | Test Run 1 | Test Run 2 | Test Run 3 | Test Run 4 | Test Run 5 | Test Run 6 | Test Run 7 | Test Run 8 | Test Run 9 | Test Run 10 |
| ------- | ------ | ---------------- | -------------- | ------------ | ------- | ------ | ------ | ------ | ------ | ------- |
|  Tests Planned | 3 | 9 | 9 | 9 | 9 | 9 | 10 | 11 | 12 | 13 |
| Tests Executed | 3 | 9 | 9 | 9 | 9 | 9 | 10 | 11 | 12 | 13 |
| Tests Passed | 0 | 2 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| Defects Found | 0 | 7 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 
| Defects Fixed | 0 | 0 | 6 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
