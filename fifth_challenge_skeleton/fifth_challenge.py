class ListChanger:
    def __init__(self, input_list: list):
        self._list = input_list

    def reverse_list(self):
        return self._list[::-1]

    def has_duplicates(self):
        set_list = list(set(self._list))
        if len(self._list) == len(set_list):
            return False
        else:
            return True

    def smallest_number(self):
        if (all([isinstance(x, int) for x in self._list]) or
                all([isinstance(x, float) for x in self._list])):
            return min(self._list)
        else:
            raise TypeError("Method only intended for numbers")

    def greatest_number(self):
        if (all([isinstance(x, int) for x in self._list]) or
                all([isinstance(x, float) for x in self._list])):
            return max(self._list)
        else:
            raise TypeError("Method only intended for numbers")

    def second_greatest_number(self):
        if (all([isinstance(x, int) for x in self._list]) or
                all([isinstance(x, float) for x in self._list])):
            unique_list = list(set(self._list))
            return sorted(unique_list, reverse=True)[1]
        else:
            raise TypeError("Method only intended for numbers")

    def remove_first_and_last(self):
        return self._list[1:-1]

