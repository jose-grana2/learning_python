def checkPassword(password):
    minChars = 12
    if (len(str(password)) >= minChars):
        if (has_mayus_and_min(password)):
            if (has_numbers(password)):
                if (has_alfanumeric(password)):
                    return True
    
    return False

def has_mayus_and_min(password):
    is_mayus = any(p.isupper() for p in password)  # Comprueba si hay alguna letra mayúscula
    is_min = any(p.islower() for p in password)  # Comprueba si hay alguna letra minúscula
    return is_mayus and is_min

def has_numbers(password):
    return any(p.isdigit() for p in password)

def has_alfanumeric(password):
    return (not p.isalnum() for p in password)




#TESTING
# print(checkPassword('hola')) #False
# print(checkPassword('hola123')) #False
# print(checkPassword('hola123.')) #False
# print(checkPassword('Hola123.')) #False
# print(checkPassword('HOLA123.')) #False
# print(checkPassword('Holaquetalcomoestas123.')) #True
