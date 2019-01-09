class Rational:
    def __init__(self, num, denom):
        self.numerator = num
        self.denominator = denom

    def __add__(self, other):
        new_numerator = self.numerator * other.denominator + \
                        self.denominator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Rational(new_numerator, new_denominator)

    def __ge__(self, other):
        return self.numerator * other.denominator >= \
               self.denominator * other.numerator

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)


fuel_needed = Rational(42, 1000)
tank1 = Rational(35, 1000)
tank2 = Rational(7, 1000)

if tank1 + tank2 >= fuel_needed:
    print("True")
else:
    print("False")

print(tank2)
print(str(tank1))
