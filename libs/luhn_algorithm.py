"""
Validate card numbers with the Luhn algorithm

Return ``VALID!`` when *card_number* passes the Luhn check.
Spaces and hyphens are allowed as formatting characters.  The rightmost
digit is the check digit, so doubling starts with the digit immediately
to its left and continues with every other digit moving left.
"""


def verify_card_number(card_number):
    if not isinstance(card_number, str):
        return "INVALID!"

    digits = card_number.replace("-", "").replace(" ", "")

    if not digits or not digits.isdigit():
        return "INVALID!"

    total = 0
    for position, digit in enumerate(reversed(digits)):
        value = int(digit)

        if position % 2 == 1:
            value *= 2
            if value > 9:
                value -= 9
        total += value

    return "VALID!" if total % 10 == 0 else "INVALID!"
