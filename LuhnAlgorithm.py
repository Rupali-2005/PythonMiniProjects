def verify_card_number(card_number):
    """Verify a credit card number using the Luhn Algorithm"""
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)  # sum of digits
        sum_of_even_digits += number

    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0


def main():
    print("=== Credit Card Validator (Luhn Algorithm) ===")
    card_number = input("Enter your card number: ").strip()

    # Remove spaces and hyphens
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Ensure input is only digits
    if not translated_card_number.isdigit():
        print("Invalid input! Please enter only digits, spaces, or hyphens.")
        return

    # Validate card number
    if verify_card_number(translated_card_number):
        print("VALID card number!")
    else:
        print("INVALID card number!")


if __name__ == "__main__":
    main()
