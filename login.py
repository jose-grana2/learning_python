"""Crea un script que pida una contraseña al usuario (el script sabe cual es la contraseña correcta).
Si la contraseña es correcta el script debe darle la bienvenida al usuario. De lo contrario debe
indicarle que la contraseña es incorrecta y darle una segunda oportunidad de introducir la
contraseña. Al segundo fallo debe mostrar un mensaje de error y terminar de ejecutarse.
Cambia el script para que no distinga entre mayúsculas y minúsculas.
(Pista: Necesitarás in If Statement anidado)"""


#definir contraseña 
pasword = "Usuario0?"

input_password = input("Introduce la contraseña")

if (input_password.lower() == pasword.lower()):
    print('Que pasa bro')
else:
    input_password = input('Bro esa no es, segundo intento')
    if input_password.lower() == pasword.lower():
         print('ahora si churra')
         print('que pasa manin')
    else:
         print('ESTÁS GILIPOLLAS?')





