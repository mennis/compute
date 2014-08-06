# -*- coding: utf-8 -*-


class PointMass(object):
    """

    """
    def __init__(self, mass, designPosition, correctedPostion):
        self.mass = mass
        self.designPosition = designPosition
        self.correctedPostion = correctedPostion

if __name__ == "__main__":
    from vector import Vector
    from array import array
    NUMELEMENTS = 3
    PointMassElements = array(NUMELEMENTS)

    i = int()
    TotalMass = float()
    CombinedCG = Vector()
    FirstMoment = Vector()

    TotalMass = 0
    # for i in range(NUMELEMENTS):



