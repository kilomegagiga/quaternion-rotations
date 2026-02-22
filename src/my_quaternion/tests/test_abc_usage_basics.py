from abc import ABC, abstractmethod

class AAA(ABC):
  @abstractmethod
  def aaa(self, a, b, c):
    pass

class BBB(AAA):
  def aaa(self, a, b, c):
    return (a, b, c)

class CCC(AAA):
  def aaa(self, a, b, c):
    return(c, b, a)


class Test_EachConcreteClass:
  def test_implementsTheAbstractMethod(self):
    objList = [ BBB(), CCC() ]
    result = []
    for obj in objList:
      result.append(len(obj.aaa(1,2,3)))
    assert result == [3, 3]
    
  def test_evaluatesItsRespectiveMethod(self):
    expect = (1,2,3)
    bbb = BBB()
    ccc = CCC()
    assert bbb.aaa(1,2,3) == expect and ccc.aaa(1,2,3) == expect[::-1]


