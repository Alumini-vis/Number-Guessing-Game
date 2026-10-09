def verify_card_number(card_number):

    card_number = card_number.replace(" ", "").replace("-", "")

    digits = [int(digit) for digit in str(card_number)]

    total = 0

    # Starting from the right, double every second digit
    # (Excluding the check digits)

    for i, digit in enumerate(reversed(digits)):
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit

    # check whether the total is a multiple of 10
    if total % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"


print(verify_card_number("453914889"))
print(verify_card_number("4111-1111-1111-1111"))
print(verify_card_number("453914881"))
print(verify_card_number("1234 5678 9012 3456"))
