# UC9 – Implement Binary Search on rotated sorted array

from typing import List


class BinarySearch:
    """Class to implement Binary Search on rotated sorted array."""

    @staticmethod
    def search(data: List[int], target: int) -> int:
        """
        Searches target in rotated sorted array.

        :param data: Rotated sorted list
        :param target: Element to search
        :return: Index or -1
        """
        low: int = 0
        high: int = len(data) - 1

        while low <= high:
            mid: int = (low + high) // 2

            if data[mid] == target:
                return mid

            # Left half is sorted
            if data[low] <= data[mid]:
                if data[low] <= target < data[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if data[mid] < target <= data[high]:
                    low = mid + 1
                else:
                    high = mid - 1

        return -1


def main() -> None:
    """Main execution function."""
    data: List[int] = [4, 5, 6, 7, 0, 1, 2]
    target: int = 0

    print("Rotated Array:", data)
    print("Target:", target)

    index: int = BinarySearch.search(data, target)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()