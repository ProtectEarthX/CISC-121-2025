"""Search algorithms for the Algorithms Course."""

from typing import Sequence, Any


def binary_search(sequence: Sequence[Any], target: Any) -> int:
    """Return the index of ``target`` in a sorted ``sequence`` or ``-1`` if not found."""
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = sequence[mid]

        if guess == target:
            return mid
        if guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1
