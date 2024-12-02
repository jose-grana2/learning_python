#Definimos las constantes
nombre1 = 'Alejandro'
nombre2 = 'Naomi'
nombre3 = 'Sergio'
saludo = 'Hola <nombre> eres una máquina'

#Nombre de entrada
name_input = input('¿Que usuario deseas usar?')

#normalizamos la entrada del contenido
name_input = name_input.replace('.', '')
name_input = name_input.replace('#', '')
name_input = name_input.lower()

#hacemos la comprobación del código
if (name_input == nombre1.lower()):
    saludo = saludo.replace('<nombre>', name_input)
elif (name_input == nombre2.lower()):
    saludo = saludo.replace('<nombre>', name_input)
elif (name_input == nombre2.lower()):
    saludo = saludo.replace('<nombre>', name_input)
else:
    saludo = saludo.replace('<nombre>', 'INVITADISIMO')

print(saludo)
