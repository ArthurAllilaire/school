import unittest
import numpy as np
from pathfinder import grid, sp, fp, cp
from surrounding import calc_weight, surrounding, addBP


class SurroundingTestClass(unittest.TestCase):
    def setUp(self):
        self.weight_func = calc_weight({}, (5, 5))
        self.test_weight = self.weight_func((0, 0))

        self.weights = surrounding(cp, grid, self.weight_func)

    def testWeight(self):
        print(self.test_weight)
        self.assertAlmostEqual(self.test_weight, 7.0710678118654755)

    def testSurroundingFunc(self):
        print(self.weights)
        self.assertAlmostEqual(
            self.weights,
            {(0, 1): 6.4031242374328485,
             (1, 0): 6.4031242374328485,
             (1, 1): 5.656854249492381})


class SetupTestClass(unittest.TestCase):
    def setUp(self):
        self.grid = np.array([[0]*5]*5)
        # Blocked positions
        bp = [(2, 2), (1, 2)]
        # Modifies the original grid
        addBP(bp, self.grid)

    def testGrid(self):
        comparison = self.grid == np.array([[0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 1, 1, 0, 0],
                                            [0, 0, 0, 0, 0],
                                            [0, 0, 0, 0, 0]])
        self.assertTrue(comparison.all())


if __name__ == '__main__':
    unittest.main()
