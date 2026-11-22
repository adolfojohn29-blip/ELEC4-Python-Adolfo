# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P6 - Recursion Toolkit
# Date: November 23, 2026


# Base case: factorial(0) returns 1.
# Recursive call: factorial(n - 1) works on a smaller number.
def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)


# Base case: sum_numbers(0) returns 0.
# Recursive call: sum_numbers(n - 1) adds the smaller numbers.
def sum_numbers(n):
    if n == 0:
        return 0

    return n + sum_numbers(n - 1)


# Base cases: the first term is 0 and the second term is 1.
# Recursive calls: add the two preceding Fibonacci terms.
def fibonacci(n):
    if n == 1:
        return 0

    if n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


# Base case: an empty list means the target was not found.
# Recursive call: if the first item does not match, search the remaining items.
def search(items, target):
    if not items:
        return False

    if items[0] == target:
        return True

    return search(items[1:], target)


def main():
    print("=== P6 Recursion Toolkit ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    while True:
        print("\n1. Factorial")
        print("2. Sum from 1 to n")
        print("3. Fibonacci")
        print("4. Recursive search")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "5":
            break

        if choice == "4":
            values = input("Enter items separated by commas: ")
            items = [item.strip() for item in values.split(",") if item.strip()]
            target = input("Enter the item to search for: ").strip()

            if len(items) > 100:
                print("Please enter at most 100 items.")
                continue

            print(f"Search result: {search(items, target)}")
            continue

        if choice not in ("1", "2", "3"):
            print("Please choose a number from 1 to 5.")
            continue

        minimum, maximum = (1, 25) if choice == "3" else (0, 100)

        try:
            number = int(
                input(f"Enter a whole number from {minimum} to {maximum}: ")
            )
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not minimum <= number <= maximum:
            print(f"Please enter a number from {minimum} to {maximum}.")
            continue

        if choice == "1":
            print(f"Factorial of {number} = {factorial(number)}")
        elif choice == "2":
            print(f"Sum from 1 to {number} = {sum_numbers(number)}")
        else:
            terms = [fibonacci(position) for position in range(1, number + 1)]
            print(f"First {number} Fibonacci terms: {terms}")
            print(f"Fibonacci term #{number} = {terms[-1]}")


if __name__ == "__main__":
    main()