import math

## Use an abstract base class (ABC) to better allow 
## direct comparison of rotation methods

from abc import ABC, abstractmethod

class PhysicalConstants():
  def m_a():
    amu = 1.660538921e-27
    A1 = 9.012
    MA = A1*amu
    return MA

  def m_b():
    amu = 1.660538921e-27
    A2 = 183.84
    MB = A2*amu
    return MB

class RotationMethod(ABC):
  @abstractmethod
  def rotate(self, randPhi, randPsi, MA, MB):
    pass

## rotate(0.7, table[j], MA, MB)
class EulerAngleMethod(RotationMethod):
  def rotate(self, u, randPhi, randPsi, MA, MB):
    phi = 2.0*math.pi*randPhi
    theta = math.pi*randPsi
    sth = math.sin(theta)
    cth = math.cos(theta)
    sth2 = math.sin(theta/2.0)
    PSI = math.atan2(sth,(MA/MB + cth))

    Qa = u[0]
    Qb = u[1]
    Qg = u[2]

    recipQnorm = 1.0/math.sqrt(Qa*Qa + Qb*Qb + Qg*Qg)
    ca = Qa*recipQnorm
    cb = Qb*recipQnorm
    cg = Qg*recipQnorm

    sa = math.sin(math.acos(ca))

    cphi = math.cos(phi)
    sphi = math.sin(phi)

    cPSI = math.cos(PSI)
    sPSI = math.sin(PSI)

    ca1 = (cPSI*ca + sPSI*sa*(cphi))
    cb1 = (cPSI*cb - sPSI/sa*(cphi*ca*cb - sphi*cg))
    cg1 = (cPSI*cg - sPSI/sa*(cphi*ca*cg + sphi*cb))

    recipQnorm = 1.0/math.sqrt(ca1*ca1 + cb1*cb1 + cg1*cg1)
    Qa = ca1*recipQnorm
    Qb = cb1*recipQnorm
    Qg = cg1*recipQnorm

    return (Qa, Qb, Qg)




