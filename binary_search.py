# UC3 – Handle element not found case with proper return value

from typing import List


class BinarySearch:
    """Class to implement Binary Search with not-found handling."""

    @staticmethod
    def search(data: List[int], target: int) -> int:
        """
        Searches for target and returns index or -1 if not found.

        :param data: Sorted list of integers
        :param target: Element to search
        :return: Index or -1
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
    target: int = 50  # not present

    print("Array:", data)
    print("Target:", target)

    index: int = BinarySearch.search(data, target)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found (returned -1)")


if __name__ == "__main__":
    main()