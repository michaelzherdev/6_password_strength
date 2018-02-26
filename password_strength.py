import sys
import re

def get_password_strength(password):
    if len(password) == 0:
        return 0

    strength = 1
    if len(password) > 8:
        strength += 2
    elif 6 <= len(password) <= 8:
        strength += 1
    if not password.isdigit():
        strength += 1
        if re.search('\d', password):
            strength += 2
    if not (password.isupper() or password.islower()):
        strength += 2
    if re.search('[@#$]', password):
            strength += 2
    return strength


if __name__ == '__main__':
    print('Password strength: %s' % get_password_strength(sys.argv[1]))
