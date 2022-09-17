### Assignment 2a

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