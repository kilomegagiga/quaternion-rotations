import numpy as np
import quaternion


## Implemented quaternion operations:
## add, subtract, multiply, divide, 
## log, exp, power, negative, conjugate,
## copysign, equal, not_equal, less, less_equal, 
## isnan, isinf, isfinite, absolute

## Other quaternion operations:
## as_float_array

class Test_AddingQuaternion:
  def test_toItsConjugateGivesTwiceTheRealPart(self):
    q1 = np.quaternion(1,1,1,1)
    q2 = q1.conjugate()
    result = q1 + q2
    expect = np.quaternion(2,0,0,0)
    assert expect == result

  def test_toNegativeOfItsConjugateGivesTwiceTheImaginaryPart(self):
    q1 = np.quaternion(1,1,1,1)
    q2 = - q1.conjugate()
    result = q1 + q2
    expect = np.quaternion(0,2,2,2)
    assert expect == result

class Test_MultiplyingQuaternion:
  def test_byConjungateIsSquareOfAbs_W(self):
    q1 = np.quaternion(3,0,0,0)
    q2 = q1.conjugate()
    result = q1 * q2
    expect = np.quaternion(9,0,0,0)
    assert expect == result
   
  def test_byConjungateIsSquareOfAbs_YZ(self):
    q1 = np.quaternion(0,0,1,1)
    q2 = q1.conjugate()
    result = q1 * q2
    expect = np.quaternion(2,0,0,0)
    assert expect == result
   
  def test_byAnotherGivesTheCrossProduct(self):
    q1 = np.quaternion(0,0,0,1)
    q2 = np.quaternion(0,1,0,1)
    q3 = q1 * q2
    result = (q3 - q3.conjugate())/2.
    expect = np.quaternion(0,0,1,0)
    assert expect == result

  def test_byAnotherGivesTheNegativeOfDotProduct(self):
    q1 = np.quaternion(0,0,0,1)
    q2 = np.quaternion(0,1,0,1)
    q3 = q1 * q2
    result = (q3 + q3.conjugate())/2
    expect = np.quaternion(-1,0,0,0)
    assert expect == result

