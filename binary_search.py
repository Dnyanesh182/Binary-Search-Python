# UC1 – Implement Binary Search using iterative approach on a sorted array

from typing import List


class BinarySearch:
    """Class to implement iterative Binary Search."""

    @staticmethod
    def search(data: List[int], target: int) -> int:
        """
        Searches for target in sorted list using iterative Binary Search.

        :param data: Sorted list of integers
        :param target: Element to search
        :return: Index of target or -1 if not found
        """
        low: int = 0
        high: int = len(data) - 1

        while low <= high:
            mid: int = (low + high) // 2

            if data[mid] == target:
                return mid
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


def main() -> None:
    """Main execution function."""
    data: List[int] = [11, 12, 22, 25, 34, 64, 90]
    target: int = 25

    print("Array:", data)
    print("Target:", target)

    index: int = BinarySearch.search(data, target)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()