# UC4 – Count number of comparisons performed during search

from typing import List, Tuple


class BinarySearch:
    """Class to implement Binary Search with comparison counting."""

    @staticmethod
    def search(data: List[int], target: int) -> Tuple[int, int]:
        """
        Searches for target and counts comparisons.

        :param data: Sorted list
        :param target: Element to search
        :return: (index, comparisons)
        """
        low: int = 0
        high: int = len(data) - 1
        comparisons: int = 0

        while low <= high:
            mid: int = (low + high) // 2
            comparisons += 1

            if data[mid] == target:
                return mid, comparisons
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1, comparisons


def main() -> None:
    """Main execution function."""
    data: List[int] = [11, 12, 22, 25, 34, 64, 90]
    target: int = 34

    print("Array:", data)
    print("Target:", target)

    index, comparisons = BinarySearch.search(data, target)

    if index != -1:
        print(f"Element found at index: {index}")
    else:
        print("Element not found")

    print("Total Comparisons:", comparisons)


if __name__ == "__main__":
    main()