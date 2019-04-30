import ast
from typing import Dict, Tuple

import c


# print(f'type of "c"" object is: {type(c)}')
# print(f'name of "c"" object is: {c.__name__}')


def parse_string_dict(string_dict: str) -> Dict:
    """Convert a String representation of a Dictionary to a dict object."""
    try:
        return ast.literal_eval(string_dict)
    except (ValueError, SyntaxError):
        raise TypeError('Given input should be String representation of a Dictionary.')


def calculate_dict_stat(input_dict: Dict) -> Tuple[int or float, int or float]:
    """Calculates dict statistics: the sum of values and the sum of values squares."""
    return c.sum_dict_values(input_dict), c.sum_dict_square_values(input_dict)

# import importlib
#
#
# importlib.reload(c)
