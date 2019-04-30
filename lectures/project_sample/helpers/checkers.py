from typing import Any


def check_input(x: Any) -> bool:
    """Checks that given input is int or float."""
    return isinstance(x, int) or isinstance(x, float)
