# UC10 – Refactor Binary Search implementation using clean code practices and reusable functions

from typing import List, TypeVar, Callable, Optional

T = TypeVar("T")


class BinarySearch:
    """Refactored, generic Binary Search implementation."""

    @staticmethod
    def search(
        data: List[T],
        target,
        key: Optional[Callable[[T], int]] = None,
    ) -> int:
        """
        Generic Binary Search with optional key.

        :param data: Sorted list
        :param target: Target value
        :param key: Optional key function
        :return: Index or -1
        """
        if not data:
            return -1

        key_func: Callable[[T], int] = key if key else lambda x: x

        return BinarySearch._binary_search(data, target, key_func)

    @staticmethod
    def _binary_search(
        data: List[T],
        target,
        key: Callable[[T], int],
    ) -> int:
        """Reusable binary search logic."""
        low: int = 0
        high: int = len(data) - 1

        while low <= high:
            mid: int = (low + high) // 2
            mid_value = key(data[mid])

            if mid_value == target:
                return mid
            elif target < mid_value:
                high = mid - 1
            else:
                low = mid + 1

        return -1


def main() -> None:
    """Main execution function."""
    data: List[int] = [11, 12, 22, 25, 34, 64, 90]

    print("Original List:", data)

    index = BinarySearch.search(data, 25)

    print("Search Result Index:", index)


if __name__ == "__main__":
    main()