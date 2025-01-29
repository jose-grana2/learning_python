class Vuelo():
    def __init__(self, id_vuelo, origen, destino, cap_max, list_pasajeros = []):
        self.id_vuelo = id_vuelo
        self.origen = origen
        self.destino = destino
        self.cap_max = cap_max
        self.list_pasajeros = list_pasajeros

    def agregar_pasajero(self, pasajero):
        if (pasajero != ''):
            if (self.asientos_libres()):
                self.list_pasajeros.append(pasajero)
                print('Pasajero añadido correctamente')
            else:
                print('Pasajero no añadido')
        else:
            print('Debe insertar un pasajero')

    def asientos_libres(self):
        num_pasajeros = len(self.list_pasajeros)
        
        if (num_pasajeros < self.cap_max):
            print('Aún hay asientos', self.cap_max - num_pasajeros, 'disponibles')
            return True
        else:
            print('Asientos completos')
            return False


