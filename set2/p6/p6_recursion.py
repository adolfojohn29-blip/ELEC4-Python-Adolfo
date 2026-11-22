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


def main():
    print("=== P6 Recursion Toolkit ===")
    print("John Nicole R Adolfo | IV-BSIT A")

    while True:
        print("\n1. Factorial")
        print("2. Sum from 1 to n")
        print("3. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "3":
            break

        if choice not in ("1", "2"):
            print("Please choose 1, 2, or 3.")
            continue

        try:
            number = int(input("Enter a whole number from 0 to 100: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if not 0 <= number <= 100:
            print("Please enter a number from 0 to 100.")
            continue

        if choice == "1":
            print(f"Factorial of {number} = {factorial(number)}")
        else:
            print(f"Sum from 1 to {number} = {sum_numbers(number)}")


if __name__ == "__main__":
    main()