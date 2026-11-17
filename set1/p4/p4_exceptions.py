
# Name: John Nicole R Adolfo
# Section: IV-BSIT A
# Activity: P4 - Safe Menu Program
# Date: November 17, 2026


# Function for dividing two numbers
def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2

    except ValueError:
        print("Error: Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")

    else:
        print(f"Division Result: {result:.2f}")

    finally:
        print("Division operation completed.")


# Function for opening and reading a file
def open_file():
    filename = input("Enter file name: ").strip()

    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Error: File not found!")

    except PermissionError:
        print("Error: Permission denied!")

    except IsADirectoryError:
        print("Error: Please enter a file, not a folder!")

    else:
        print("\n=== FILE CONTENTS ===")
        print(content)

    finally:
        print("File operation completed.")


# Main menu
def main():
    while True:
        print("\n=== SAFE MENU PROGRAM ===")
        print("1. Divide Two Numbers")
        print("2. Open a File")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            divide_numbers()

        elif choice == "2":
            open_file()

        elif choice == "3":
            print("Thank you for using the program!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
