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
    m1.rotate(u1,randPhi,randPsi,phys.m_a(),phys.m_b())
    ## u1 = direction of travel
    ## u2 = deflectionCalculation(u1, 0)
    ## assert u2 == u1
    assert False  ## not yet implemented

  def test_piRadiansResultsInReflectedVector(self):
    ## u1 = direction of travel
    ## u2 = deflectionCalculation(u1, math.pi)
    ## assert u2 == -u1 
    assert False  ## not yet implemented


