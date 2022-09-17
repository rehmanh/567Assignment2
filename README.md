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
|  testRightTriangleA | 3, 4, 5 | Right | InvalidInput | Fail |
| testRightTriangleB | 5, 3, 4 | Right | InvalidInput | Fail |
| testEquilateralTriangles | 1, 1, 1 | Equilateral | InvalidInput | Fail |
| testInvalidInputA | 201, 202, 203 | InvalidInput | InvalidInput | Pass |
| testInvalidInputB | -1, -4, -5 | InvalidInput | InvalidInput | Pass |
| testInvalidInputC | foo, bar, baz | InvalidInput | ERROR | Fail |
| testNotATriangle | 1, 1, 2 | NotATriangle | InvalidInput | Fail |
| testScaleneTriangle | 7, 12, 15 | Scalene | InvalidInput | Fail |
| testIsoscelesTriangle | 4, 4, 6 | Isosceles | InvalidInput | Fail |

#### Assignment Summary

| - | Test Run 1 | Test Run 2 | Test Run 3 | Test Run 4 | Test Run 5 | Test Run 6 | Test Run 7 | Test Run 8 | Test Run 9 | Test Run 10 |
| ------- | ------ | ---------------- | -------------- | ------------ | ------- | ------ | ------ | ------ | ------ | ------- |
|  Tests Planned | 3 | 9 | 9 | 9 | 9 | 9 | 10 | 11 | 12 | 13 |
| Tests Executed | 3 | 9 | 9 | 9 | 9 | 9 | 10 | 11 | 12 | 13 |
| Tests Passed | 0 | 2 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
| Defects Found | 0 | 7 | 3 | 2 | 1 | 0 | 0 | 0 | 0 | 0 | 
| Defects Fixed | 0 | 0 | 6 | 1 | 1 | 1 | 0 | 0 | 0 | 0 |
