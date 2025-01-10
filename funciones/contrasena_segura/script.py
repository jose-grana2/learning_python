import creator
import validator
res = 'No'
password = validator.checkPassword(input('Introduce una contraseña para comprobar su seguridad '))

if (password):
    print('Tu contraseña es segura')
    res = input('¿Quiere generar otra contraseña segura de forma automática? (Si/No) ')
else:
    print('Tu contraseña no es segura')
    res = input('¿Quiere generar una contraseña segura de forma automática? (Si/No) ')

if (res == 'Si'):
    length = int(input('¿Qué longitud tendrá la contraseña? (Le recomendamos que mínimo tenga 12 caracteres) '))
    upper = bool(input('¿Quieres que contenga mayúsculas? (True/False) '))
    lower = bool(input('¿Quieres que contenga minúsculas? (True/False) '))
    number = bool(input('¿Quieres que contenga números? (True/False) '))
    specials = bool(input('¿Quieres que contenga carácteres especiales? (True/False) '))

    new_password = creator.passwordGenerator(length, has_upper=upper, has_lower=lower, has_number=number, has_specials=specials)
    print('Su nueva contraseña es ', new_password)
    if (not validator.checkPassword(new_password)):
        print('Y debe ser modificada porque no es segura')
else:
    print('')
    print('Fin del programa...')
    print('')

