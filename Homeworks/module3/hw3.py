# https://www.python.org/dev/peps/pep-0570/#logical-ordering
# Positional-only parameters also have the (minor) benefit of enforcing some logical order when
# calling interfaces that make use of them. For example, the range function takes all its
# parameters positionally and disallows forms like:

# range(stop=5, start=0, step=2)
# range(stop=5, step=2, start=0)
# range(step=2, start=0, stop=5)
# range(step=2, stop=5, start=0)

# at the price of disallowing the use of keyword arguments for the (unique) intended order:

# range(start=0, stop=5, step=2)
"""
Write a function that accept any sequence (list, string, tuple) of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""

import string

"""
def custom_range(*args):
    output = []
    if len(args) == 4:
        step = args[3]
    else:
        step = 1
    if len(args) == 2:
        stop_index = args[0].index(args[1])
        for i in range(0, stop_index):
            output.append(args[0][i])
        return output
    else:
        stop_index = args[0].index(args[2])
        i = args[0].index(args[1])
        if step > 0:
            while i < stop_index:
                output.append(args[0][i])
                i += step
        else:
            while i > stop_index:
                output.append(args[0][i])
                i += step
        return output
"""


def custom_range(*args):
    output = []
    if len(args) == 2:
        for i in range(args[0].index(args[1])):
            output.append(args[0][i])
    elif len(args) == 3:
        for i in range(args[0].index(args[1]), args[0].index(args[2])):
            output.append(args[0][i])
    elif len(args) == 4:
        for i in range(args[0].index(args[1]), args[0].index(args[2]), args[3]):
            output.append(args[0][i])
    return output
