# UC6 – Search custom objects using Binary Search with key (e.g., search by age)

from typing import List, Callable, TypeVar

T = TypeVar("T")


class Person:
    """Represents a person with name and age."""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"({self.name}, {self.age})"


class BinarySearch:
    """Class to implement Binary Search for custom objects."""

    @staticmethod
    def search(data: List[T], target: int, key: Callable[[T], int]) -> int:
        """
        Searches for target using key function.

        :param data: Sorted list of objects
        :param target: Target key value
        :param key: Key extractor function
        :return: Index or -1
        """
        low: int = 0
        high: int = len(data) - 1

        while low <= high:
            mid: int = (low + high) // 2
            mid_value: int = key(data[mid])

            if mid_value == target:
                return mid
            elif target < mid_value:
                high = mid - 1
            else:
                low = mid + 1

        return -1


def main() -> None:
    """Main execution function."""
    people: List[Person] = [
        Person("David", 20),
        Person("Bob", 25),
        Person("Alice", 30),
        Person("Charlie", 35),
    ]

    target_age: int = 30

    print("People List:", people)
    print("Target Age:", target_age)

    index: int = BinarySearch.search(
        people, target_age, key=lambda person: person.age
    )

    if index != -1:
        print(f"Person found at index: {index} -> {people[index]}")
    else:
        print("Person not found")


if __name__ == "__main__":
    main()