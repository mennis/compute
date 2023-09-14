import unittest
import random
import numpy as np
from compute.vector import Vector


class TestCompute(unittest.TestCase):
    """
    Here we compare our math to numpy as a sanity check.
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

        self.assertEqual(np.sqrt(nV.dot(nV)), cV.magnitude)

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

    def test_reverse(self):
        """
        I do not believe this will ever be fruitful.
        """
        x = random.randint(-1000, 50000)
        y = random.randint(-1000, 50000)
        z = random.randint(-1000, 50000)

        cV = Vector(x, y, z)

        cV.reverse()

        self.assertEqual(cV.x, -x)
        self.assertEqual(cV.y, -y)
        self.assertEqual(cV.z, -z)

    def test_iadd(self):
        x1 = random.randint(-1000, 50000)
        y1 = random.randint(-1000, 50000)
        z1 = random.randint(-1000, 50000)

        cV = Vector(x1, y1, z1)

        x2 = random.randint(-1000, 50000)
        y2 = random.randint(-1000, 50000)
        z2 = random.randint(-1000, 50000)

        nV = np.add(np.array([x1, y1, z1]),
                    np.array([x2, y2, z2]))
        cV +=  Vector(x2, y2, z2)

        self.assertEqual(nV[0], cV.x)
        self.assertEqual(nV[1], cV.y)
        self.assertEqual(nV[2], cV.z)

    def test_isub(self):
        x1 = random.randint(-1000, 50000)
        y1 = random.randint(-1000, 50000)
        z1 = random.randint(-1000, 50000)

        cV = Vector(x1, y1, z1)

        x2 = random.randint(-1000, 50000)
        y2 = random.randint(-1000, 50000)
        z2 = random.randint(-1000, 50000)

        nV = np.subtract(np.array([x1, y1, z1]),
                         np.array([x2, y2, z2]))

        cV -= Vector(x2, y2, z2)

        self.assertEqual(nV[0], cV.x)
        self.assertEqual(nV[1], cV.y)
        self.assertEqual(nV[2], cV.z)

    def test_imult(self):
        x1 = random.randint(-1000, 50000)
        y1 = random.randint(-1000, 50000)
        z1 = random.randint(-1000, 50000)

        cV = Vector(x1, y1, z1)

        x2 = random.randint(-1000, 50000)
        y2 = random.randint(-1000, 50000)
        z2 = random.randint(-1000, 50000)

        nV = np.multiply(np.array([x1, y1, z1]),
                         np.array([x2, y2, z2]))

        cV *= Vector(x2, y2, z2)

        self.assertEqual(nV[0], cV.x)
        self.assertEqual(nV[1], cV.y)
        self.assertEqual(nV[2], cV.z)


    def test_idiv(self):
        x1 = random.randint(-1000, 50000)
        y1 = random.randint(-1000, 50000)
        z1 = random.randint(-1000, 50000)

        cV = Vector(x1, y1, z1)

        x2 = random.randint(-1000, 50000)
        y2 = random.randint(-1000, 50000)
        z2 = random.randint(-1000, 50000)

        nV = np.divide(np.array([float(x1), float(y1), float(z1)]),
                       np.array([x2, y2, z2]))

        cV /= Vector(x2, y2, z2)

        self.assertAlmostEqual(nV[0], cV.x)
        self.assertAlmostEqual(nV[1], cV.y)
        self.assertAlmostEqual(nV[2], cV.z)

if __name__ == '__main__':
    unittest.main()
