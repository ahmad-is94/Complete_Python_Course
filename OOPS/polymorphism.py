#using complex numbers
class Complex:
    def __init__(self,real,imag):
        self.real =real
        self.imag = imag

    def display(self):
        print(self.real,'i +',self.imag,'j')

    def add(self,c2):
        newreal = self.real + c2.real
        newimag = self.imag + c2.imag
        return Complex(newreal,newimag)



c1  = Complex(1,2)
c1.display()
c2 = Complex(3,4)
c2.display()
c3 = c1.add(c2)
c3.display()


#by usimg dunder function
class Complex:
    def __init__(self,real,imag):
        self.real =real
        self.imag = imag

    def display(self):
        print(self.real,'i +',self.imag,'j')

    def __add__(self,c2):
        newreal = self.real + c2.real
        newimag = self.imag + c2.imag
        return Complex(newreal,newimag)

    def __sub__(self, c2):
        newreal = self.real - c2.real
        newimag = self.imag - c2.imag
        return Complex(newreal, newimag)

    def __mul__(self, c2):
        newreal = self.real * c2.real
        newimag = self.imag * c2.imag
        return Complex(newreal, newimag)

    def __mod__(self, c2):
        newreal = self.real / c2.real
        newimag = self.imag / c2.imag
        return Complex(newreal, newimag)


c1  = Complex(1,2)
c1.display()
c2 = Complex(3,4)
c2.display()
c3 = c1 + c2
c4 = c1 - c2
c5 = c1 * c2
c6 = c1 / c2
c3.display()
c4.display()
c5.display()
c6.display()