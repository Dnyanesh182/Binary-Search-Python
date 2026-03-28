# UC8 – Compare Binary Search performance with Linear Search

from typing import List
import time


class BinarySearch:
    @staticmethod
    def search(data: List[int], target: int) -> int:
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            if data[mid] == target:
                return mid
            elif target < data[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1


class LinearSearch:
    @staticmethod
    def search(data: List[int], target: int) -> int:
        for i, value in enumerate(data):
            if value == target:
                return i
        return -1


def compare(size: int) -> None:
    """Compare Binary Search vs Linear Search."""
    data: List[int] = list(range(size))
    target: int = data[-1] if data else -1

    start = time.time()
    BinarySearch.search(data, target)
    binary_time = time.time() - start

    start = time.time()
    LinearSearch.search(data, target)
    linear_time = time.time() - start

    print(f"Input Size: {size}")
    print(f"Binary Search: {binary_time:.6f}s")
    print(f"Linear Search: {linear_time:.6f}s")
    print("-" * 40)


def main() -> None:
    """Main execution function."""
    sizes: List[int] = [10, 100, 1000, 10000]

    print("Performance Comparison: Binary Search vs Linear Search")
    for size in sizes:
        compare(size)


if __name__ == "__main__":
    main()