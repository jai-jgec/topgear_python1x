class ComplexCompute ():
    def __init__(self, realPart, imagPart):
        self.realPart = realPart
        self.imagPart = imagPart
    def __add__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = r1+r2
        resultI = i1+i2
        result = complex(resultR, resultI)
        return result
    def __sub__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = r1-r2
        resultI = i1-i2
        result = complex(resultR, resultI)
        return result
    def __mul__(self, other):
        r1 = self.realPart
        i1 = self.imagPart
        r2 = other.realPart
        i2 = other.imagPart
        resultR = (r1*r2-i1*i2)
        resultI = (r1*i2+r2*i1)
        result = complex(resultR, resultI)
        return result    
    def __div__(self,other):
      r1 = self.realPart
      i1 = self.imagPart
      r2 = other.realPart
      i2 = other.imagPart
      print complex(r1,i1),'/',complex(r2,i2)
      

c1 = ComplexCompute(2,3)
c2 = ComplexCompute(1,4)
print c1+c2
print c1-c2
print c1*c2
c1/c2