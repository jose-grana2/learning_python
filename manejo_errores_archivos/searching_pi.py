"""BUSCANDO EN PI
Busca si tu fecha de nacimiento esta en los primeros 10000 digitos de pi (y
en que posición. Puedes usar find()).
Puedes usar el archivo pi_10000.txt"""

file = 'pi_10000.txt'

birthday = input('Enter your birthday (without separators)')

with open(file) as pi:
    digits = pi.read()
    position = digits.find(birthday)
    print(position)

if (position == -1):
    print('Your birthday is not in the number pi')
else: 
    print('Your birthday is in the number pi')