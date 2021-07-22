"""Coding Challenge Skeleton #2
"""


class Car:
    def __init__(self):
        self._speed = 0
        self._start_car = False

    def start_car(self):
        # Todo: implement me
        self._start_car = True

    def turn_off_car(self):
        # Todo: implement me
        self._start_car = False

    def add_speed(self):
        self._speed += 5

    def remove_speed(self):
        # Todo: implement me
        self._speed -= 5

    def current_speed(self):
        return self._speed

    def stop(self):
        self._speed = 0

    def car_status(self):
        return self._start_car
