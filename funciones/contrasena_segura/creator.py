import random, string

def passwordGenerator(length, **specs):
    chars = ''
    if (specs['has_upper']):
       chars += string.ascii_uppercase

    if (specs['has_lower']):
       chars += string.ascii_lowercase

    if (specs['has_number']):
        chars += string.digits

    if (specs['has_specials']):
       chars += string.punctuation

    if (specs['has_upper']):
       chars += string.ascii_uppercase
    

    password = ''.join(random.choice(chars) for _ in range(length))

    return password

# print(passwordGenerator(33, has_upper=False, has_lower=True, has_number=True, has_specials=True))


