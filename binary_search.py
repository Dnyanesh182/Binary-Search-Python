# UC5 – Apply Binary Search on list of strings (lexicographical order)

from typing import List


class BinarySearch:
    """Class to implement Binary Search for strings."""

    @staticmethod
    def search(data: List[str], target: str) -> int:
        """
        Searches for target string in sorted list.

        :param data: Sorted list of strings
        :param target: String to search
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
    data: List[str] = ["apple", "banana", "cherry", "date"]
    target: str = "cherry"

    print("Array:", data)
    print("Target:", target)

    index: int = BinarySearch.search(data, target)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")


if __name__ == "__main__":
    main()