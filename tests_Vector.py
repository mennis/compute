import unittest
import random
import numpy as np
from vector import Vector


class TestCompute(unittest.TestCase):
    """
    Here we use numpy to check our math.
    """

    def setUp(self):
        """
        create a randomish vector
        """
        random.seed()

    def test_magnitude(self):
        x = random.randint(-1000, 50000)
        y = random.randint(-1000, 50000)
        z = random.randint(-1000, 50000)

        nV = np.array([x, y, z])
        cV = Vector(x, y, z)

        self.assertEquals(np.sqrt(nV.dot(nV)), cV.magnitude)

    def test_normalize(self):
        x = random.randint(-1000, 50000)
        y = random.randint(-1000, 50000)
        z = random.randint(-1000, 50000)

        nV = np.array([x, y, z])
        cV = Vector(x, y, z)

        n = nV / np.linalg.norm(nV)

        cV.normalize()
        self.assertAlmostEqual(n[0], cV.x)
        self.assertAlmostEqual(n[1], cV.y)
        self.assertAlmostEqual(n[2], cV.z)

if __name__ == '__main__':
    unittest.main()

