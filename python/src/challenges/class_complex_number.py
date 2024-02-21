import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imag = imaginary
        self.c = complex(real, imaginary)
        
    def __add__(self, no):
        _ = self.c + no.c
        return Complex(_.real, _.imag)
        
    def __sub__(self, no):
        _ = self.c - no.c
        return Complex(_.real, _.imag)
        
    def __mul__(self, no):
        _ = self.c * no.c
        return Complex(_.real, _.imag)

    def __truediv__(self, no):
        _ = self.c / no.c
        return Complex(_.real, _.imag)

    def mod(self):
        _ = abs(self.c) # in complex analysis, the modulus is the absolute value
        return Complex(_.real, _.imag)

    def __str__(self):
        if self.imag == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imag >= 0:
                result = "0.00+%.2fi" % (self.imag)
            else:
                result = "0.00-%.2fi" % (abs(self.imag))
        elif self.imag > 0:
            result = "%.2f+%.2fi" % (self.real, self.imag)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imag))
        return result

if __name__ == '__main__':
    c = map(float, [2, 1])
    d = map(float, [5, 6])
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')