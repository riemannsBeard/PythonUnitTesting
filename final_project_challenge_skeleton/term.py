class Term:
    def __init__(self, coefficient, power):
        self._coefficient = coefficient
        self._power = power

    def get_power(self):
        if self._power is not None:
            return self._power
        else:
            raise TypeError('Please, make sure that a valid power is passed.')

    def get_coefficient(self):
        if self._coefficient is not None:
            return self._coefficient
        else:
            raise TypeError('Please, make sure that a valid coefficient is passed.')

