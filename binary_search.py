# UC7 – Analyze time complexity of Binary Search with different input sizes

from typing import List
import time


class BinarySearch:
    """Class to implement Binary Search."""

    @staticmethod
    def search(data: List[int], target: int) -> int:
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


def analyze_performance(sizes: List[int]) -> None:
    """Analyze execution time for Binary Search."""
    for size in sizes:
        data: List[int] = list(range(size))  # already sorted
        target: int = data[-1] if data else -1

        start_time: float = time.time()
        BinarySearch.search(data, target)
        end_time: float = time.time()

        print(f"Input Size: {size}, Time Taken: {end_time - start_time:.6f} seconds")


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [10, 100, 1000, 10000]

    print("Binary Search Time Complexity Analysis:")
    analyze_performance(sizes)


if __name__ == "__main__":
    main()