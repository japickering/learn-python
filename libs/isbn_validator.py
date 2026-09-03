"""
Debug an ISBN Validator
Validate ISBN-10 and ISBN-13 codes entered from the command line.
Print whether *isbn* is valid for the requested ISBN length.
"""


def validate_isbn(isbn, length):
    if len(isbn) != length:
        print(f"ISBN-{length} code should be {length} digits long.")
        return

    check_digit_index = length - 1
    main_digits = isbn[:check_digit_index]
    given_check_digit = isbn[check_digit_index]

    # ISBN-10 permits an uppercase X as its check digit; ISBN-13 does not.
    if not main_digits.isdigit() or (
        length == 10
        and not (given_check_digit.isdigit() or given_check_digit == "X")
    ) or (length == 13 and not given_check_digit.isdigit()):
        print("Invalid character was found.")
        return

    main_digits_list = [int(digit) for digit in main_digits]

    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    if given_check_digit == expected_check_digit:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")


# Return the ISBN-10 check digit for the first nine digits.
def calculate_check_digit_10(main_digits_list):
    digits_sum = sum(digit * (10 - index)
                     for index, digit in enumerate(main_digits_list))
    result = 11 - digits_sum % 11

    if result == 11:
        return "0"

    if result == 10:
        return "X"

    return str(result)


# Return the ISBN-13 check digit for the first twelve digits
def calculate_check_digit_13(main_digits_list):
    digits_sum = sum(
        digit * (1 if index % 2 == 0 else 3)
        for index, digit in enumerate(main_digits_list)
    )
    result = 10 - digits_sum % 10
    return "0" if result == 10 else str(result)


def main():
    user_input = input("Enter ISBN and length: ")
    values = user_input.split(",")

    try:
        isbn = values[0]
        length = int(values[1])
    except IndexError:
        print("Enter comma-separated values.")
        return
    except ValueError:
        print("Length must be a number.")
        return

    if length in (10, 13):
        validate_isbn(isbn, length)
    else:
        print("Length should be 10 or 13.")

# comment out main() as per user stories
# main()
