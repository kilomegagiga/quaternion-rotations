import math
import random
from my_quaternion.rotation_method import PhysicalConstants as phys
from my_quaternion.rotation_method import EulerAngleMethod

class Test_DeflectionBy:
  def test_zeroRadiansResultsInOriginalVector(self):
    m1 = EulerAngleMethod()
    scale = (1/math.sqrt(1+4+9))
    u1 = (scale*1, scale*2, scale*3)
    randPhi = 0.7
    randPsi = 0.0
    u2 = m1.rotate(u1,randPhi,randPsi,phys.m_a(),phys.m_b())
    assert u2 == u1

  def test_piRadiansResultsInReflectedVector(self):
    m1 = EulerAngleMethod()
    scale = (1/math.sqrt(1+4+9))
    u1 = tuple(scale*x for x in (1, 2, 3))
    randPhi = 0.7
    randPsi = 1.0
    u2 = m1.rotate(u1,randPhi,randPsi,phys.m_a(),phys.m_b())
    error = math.sqrt(sum(tuple((a+b)**2 for a,b in zip(u1,u2))))
    ## allow for variation in the final digit of the floats
    threshold = 1e-15
    assert error < threshold


