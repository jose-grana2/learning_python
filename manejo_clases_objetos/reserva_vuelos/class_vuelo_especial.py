from class_vuelo import Vuelo


class VueloEspecial(Vuelo):
    def __init__(self, motivo_vuelo, id_vuelo, origen, destino, cap_max, list_pasajero = []):
        super().__init__(id_vuelo, origen, destino, cap_max, list_pasajero)
        self.motivo_vuelo = motivo_vuelo