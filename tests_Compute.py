import unittest
import random
import numpy as np

from compute import average, median, standard_dev, variance


class TestCompute(unittest.TestCase):
    """
    Here we use numpy to check our math.
    """

    def setUp(self):
        """
        create a randomish list of floats
        """
        random.seed()

        s = []
        for x in range(random.randint(10, 100)):
            s.append(random.randint(-1000, 50000) + random.random())

        self.s = s

    def test_standard_deviation(self):
        self.assertAlmostEquals(standard_dev(self.s), np.std(self.s), places=6)

    def test_variance(self):
        self.assertAlmostEquals(variance(self.s), np.var(self.s), places=6)

    def test_median(self):
        self.assertAlmostEquals(median(self.s), np.median(self.s), places=6)

    def test_average(self):
        self.assertAlmostEqual(average(self.s), np.average(self.s), places=6)


if __name__ == '__main__':
    unittest.main()
