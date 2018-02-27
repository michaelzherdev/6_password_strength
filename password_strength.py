import sys
import re


def get_password_strength(password):
    if not password:
        return 0

    strength = 1
    strength += _check_length_strength(password)
    strength += _check_digits(password)
    strength += _check_letters_case(password)
    return strength


def _check_length_strength(password):
    length_strength = 0
    if len(password) > 8:
        length_strength = 2
    elif 6 <= len(password) <= 8:
        length_strength = 1
    return length_strength


def _check_digits(password):
    digit_strength = 0
    if not password.isdigit():
        digit_strength += 1
        if re.search('\d', password):
            digit_strength += 2
    return digit_strength


def _check_letters_case(password):
    letters_strength = 0
    if not (password.isupper() or password.islower()):
        letters_strength += 2
    if re.search('[@#$]', password):
        letters_strength += 2
    return letters_strength


if __name__ == '__main__':
    print('Password strength: %s' % get_password_strength(sys.argv[1]))
