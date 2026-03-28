# UC2 – Implement Binary Search using recursive approach

from typing import List


class BinarySearch:
    """Class to implement recursive Binary Search."""

    @staticmethod
    def search(data: List[int], target: int) -> int:
        """
        Public method to initiate recursive search.

        :param data: Sorted list of integers
        :param target: Element to search
        :return: Index of target or -1 if not found
        """
        return BinarySearch._search_recursive(data, target, 0, len(data) - 1)

    @staticmethod
    def _search_recursive(data: List[int], target: int, low: int, high: int) -> int:
        """
        Recursive Binary Search helper.

        :param data: Sorted list
        :param target: Element to search
        :param low: Lower bound index
        :param high: Upper bound index
        :return: Index or -1
        """
        if low > high:
            return -1

        mid: int = (low + high) // 2

        if data[mid] == target:
            return mid
        elif target < data[mid]:
            return BinarySearch._search_recursive(data, target, low, mid - 1)
        else:
            return BinarySearch._search_recursive(data, target, mid + 1, high)


def main() -> None:
    """Main execution function."""
    data: List[int] = [11, 12, 22, 25, 34, 64, 90]
    target: int = 34

    print("Array:", data)
    print("Target:", target)

    index: int = BinarySearch.search(data, target)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()