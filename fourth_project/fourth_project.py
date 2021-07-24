from math import sqrt


class FibonacciSequence:

    def recursive_method(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.recursive_method(n - 1) +\
                   self.recursive_method(n - 2)

    def math_method(self, n):
        phi = (1 + sqrt(5))/2
        return (phi**n - (1 - phi)**n)/sqrt(5)
