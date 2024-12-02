"""BECAS PARA ESTUDIANTES (BONUS*):
El gobierno quiere otorgar becas de excelencia a los estudiantes con un mínimo de un 8 de media.
Además para acceder a la beca el estudiante debe tener entre 17 y 21 años. Crea un script que
pida el nombre, la edad y la nota media del estudiante e indique si puede optar a la beca o no.
*Los ejercicios bonus no se resolverán directamente en clase si no que están pensados para que
los alumnos los discutan por el chat de Discord y compartan sus soluciones. Las soluciones
compartidas de los alumnos se subirán en un archivo a la academia."""

name = input('Introduce el nombre: ')
age = int(input('Introduce la edad: '))
average_score = float(input('Introduce la nota media '))

if (age >= 17 and age <= 21):
    if (average_score >= 8):
        print(name, 'josepuedes optar por una la beca, tienes', age, 'años y de nota media:', average_score)
    else:
        print(name, 'tienes la edad válida pero no la nota media, sigue esforzándote')
else:
    print(name, 'no tienes la edad comprendida entre 17 y 21')