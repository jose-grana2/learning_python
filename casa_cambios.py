dinero_usuario = int(input('¿Cuánto dinero quieres convertir a dólares? '))

conversor  = dinero_usuario * 1.2
coste = (conversor * 10) / 100
dolares_netos = conversor - coste

print('Dinero a percibir:',  dolares_netos, 'dólares \n'
    'Costes de gestión: ', coste, 'dólares \n'
    'Dinero antes de la conversion :', conversor, 'dólares')