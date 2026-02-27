import math

def mcd(a, b):
    return math.gcd(abs(a), abs(b))

#Semplificazione
def semplifica(num, den):
    divisore=mcd(num, den)
    return num//divisore, den//divisore

class Frazione():
    def __init__ (self, num, den):
        if den == 0:
            raise ValueError("Il denominatore non può essere zero")
        
        # Normalizza segno: denominatore sempre positivo
        if den < 0:
            num = -num
            den = -den

        self.num, self.den = semplifica(num, den)

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __repr__(self):
        return f"Frazione({self.num}, {self.den})"
    
    def __add__(self, other):
        if not isinstance(other, Frazione):
            return NotImplemented

        a, b = self.num, self.den
        c, d = other.num, other.den
        num = a * d + b * c
        den = b * d
        return Frazione(num, den)

    def __sub__(self, other):
        if not isinstance(other, Frazione):
            return NotImplemented

        a, b = self.num, self.den
        c, d = other.num, other.den
        num = a * d - b * c
        den = b * d
        return Frazione(num, den)

    def __mul__(self, other):
        if not isinstance(other, Frazione):
            return NotImplemented

        a, b = self.num, self.den
        c, d = other.num, other.den
        return Frazione(a * c, b * d)

    def __truediv__(self, other):
        if not isinstance(other, Frazione):
            return NotImplemented

        a, b = self.num, self.den
        c, d = other.num, other.den
        if c == 0:
            raise ZeroDivisionError("division by zero fraction")
        return Frazione(a * d, b * c)

    def __eq__(self, other):
        if not isinstance(other, Frazione):
            return NotImplemented
        return self.num == other.num and self.den == other.den

    def to_float(self):
        return self.num / self.den


if __name__ == "__main__":
    f1 = Frazione(1, 2)
    f2 = Frazione(1, 3)

    print(f1 + f2)  # 5/6
    print(f1 - f2)  # 1/6
    print(f1 * f2)  # 1/6
    print(f1 / f2)  # 3/2

    print(f1 == Frazione(2, 4))  # True (semplificate uguali)
    print(f1.to_float())  # 0.5
