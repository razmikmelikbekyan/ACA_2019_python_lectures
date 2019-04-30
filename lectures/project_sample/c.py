from typing import Dict

from helpers.checkers import check_input
from helpers.utils.math_tools import square


# from helpers import check_input, square


# print('c is imported')


def sum_dict_values(input_dict: Dict) -> int or float:
    """Sums the values of given input dict."""
    values = list(input_dict.values())
    if not all(check_input(x) for x in values):
        raise ValueError('Given values should be int or float.')
    return sum(values)


def sum_dict_square_values(input_dict: Dict) -> int or float:
    """Sums the values of given input dict."""
    values = list(input_dict.values())
    if not all(check_input(x) for x in values):
        raise ValueError('Given values should be int or float.')
    return sum(map(square, values))
