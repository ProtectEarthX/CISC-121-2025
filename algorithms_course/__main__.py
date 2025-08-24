"""Entry point for demonstrating algorithms."""

from . import binary_search


def main() -> None:
    data = [1, 3, 5, 7, 9]
    target = 7
    index = binary_search(data, target)
    if index == -1:
        print(f"{target} not found in {data}")
    else:
        print(f"{target} found at index {index} in {data}")


if __name__ == "__main__":
    main()
