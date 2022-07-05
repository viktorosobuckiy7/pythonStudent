from math import gcd


class Fraction:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def common_factor(self):
        if self.b != 0:
            return self.a // gcd(self.a, self.b) / (self.b // gcd(self.a, self.b))
        else:
            raise ZeroDivisionError("На ноль делить нельзя")

    def __add__(self, other):
        return (self.a + other.a) / gcd(self.b + other.b)

    def __sub__(self, other):
        return (self.a - other.a) / gcd(self.b + other.b)

    def __mul__(self, other):
        return self.common_factor() * other.common_factor()

    def __gt__(self, other):
        return self.common_factor() > other.common_factor()




frt_1 = Fraction(6, 12)
frt_2 = Fraction(3, 0)

print(frt_1 > frt_2)
