def is_armstrong_number(number):
    num_digits = len(str(number))

    total = 0
    for digit in str(number):
        total = total + int(digit) ** num_digits

    return total==number
