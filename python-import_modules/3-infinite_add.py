#!/usr/bin/python3
import sys


def main():
    """Adds all arguments passed to the script and prints the result."""
    # Get all arguments except the script name
    args = sys.argv[1:]

    # Convert all arguments to integers
    numbers = [int(arg) for arg in args]

    # Sum the numbers and print
    print(sum(numbers))


if __name__ == "__main__":
    main()
