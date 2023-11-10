"""Challenge Question - Sums."""
__author__ = "730566761"


def w_sum(vals: list[float]) -> float:  # type: ignore 
    """While loops sum."""
    idx: int = 0
    while idx < len(vals): 
        return (sum(vals))
    idx += 1
    if len(vals) == 0:
        return (0.0)


def f_sum(vals: list[float]) -> float:  # type: ignore 
    """For... in... loops sum."""
    for element in vals: 
        return (sum(vals))
    if len(vals) == 0:
        return (0.0)


def f_range_sum(vals: list[float]) -> float:  # type: ignore 
    """For...in... range loops sum."""
    for idx in range(0, len(vals)):
        return (sum(vals))
    if len(vals) == 0:
        return (0.0)