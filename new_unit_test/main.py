"""
@author: Antonio Martín.
@data: Jul, 31th, 2021.
To use this class you need to do: 1 - jasfhlksahfs, 2 - fdkdhafkdhf, etc.
Ex. lc = ListChanger().

The reason why we have this class is because: 1 - jasfhlksahfs,
2 - fdkdhafkdhf, etc.
"""
import heapq


class ListChanger:
    def __init__(self, input_list: list):
        self._list = input_list

    # This method is going to return a reverse list.
    def reverse_list(self):
        return self._list[::-1]

    # This method is going to return a reverse list.
    def has_duplicates(self):
        return len(self._list) != len(set(self._list))

    # This method is going to return a reverse list.
    def smallest_number(self):
        return min(self._list)

    # This method is going to return a reverse list.
    def greatest_number(self):
        return max(self._list)

    # This method is going to return a reverse list.
    def second_greatest_number(self):
        # heapq.nlargest is going to get second largest number.
        return heapq.nlargest(2, set(self._list))[1]

    # This method is going to return a reverse list.
    def remove_first_and_last(self):
        return self._list[1:len(self._list) - 1]
