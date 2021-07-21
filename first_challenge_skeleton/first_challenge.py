"""Coding Challenge Skeleton #1
This counter function purpose is to count how many english letters does your name contain.
After writing your tests, develop the counter function as needed to pass all your tests.

"""


def counter(name: str) -> int:
    # Handle of None type AttributeError
    if name is None:
        raise AttributeError('Please, make sure that name is not of None type.')

    # Workaround to remove spaces
    name = name.replace(' ', '')
    if len(name) == 0:
        raise Exception('Please, make sure that name contains at least '
                        'one character.')

    if name.isalpha():
        return len(name)
    else:
        raise Exception('Wrong input data. Please, make sure that you are '
                        ' introducing an alpha string.')

# print(counter('Mo@!^'))
# print(counter('Iñaki'))
