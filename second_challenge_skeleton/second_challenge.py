"""Coding Challenge Skeleton #2
"""


class Car:
    def __init__(self):
        self._speed = 0
        self._start_car = False

    def start_car(self):
        if not self._start_car:
            self._start_car = True
        else:
            raise Exception('The car is already started.')

    def turn_off_car(self):
        if self.current_speed() == 0:
            self._start_car = False
        else:
            raise Exception('Please, make sure that the car is stopped before '
                            'turning it off.')

    def add_speed(self):
        self._speed += 5

    def remove_speed(self):
        if self.current_speed() >= 5:
            self._speed -= 5
        else:
            self._speed = 0

    def current_speed(self):
        return self._speed

    def stop(self):
        self._speed = 0

    def car_status(self):
        return self._start_car
