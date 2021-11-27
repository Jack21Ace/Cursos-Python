from typing import List

from enum import Enum
class Tipo(Enum):
    TITULAR = "Titular"
    SUPLENTE = "Suplente"

# Creación de clase Padre Jugadores para mantener el concepto de herencia
class Jugador:
    def __init__(self, nombre:str, posicion:str, tipo:Tipo):
        self.__nombre = nombre
        self.__posicion = posicion
        self.__tipo = tipo

# Getter and Setters
    # Get & Set nombre START
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre:str):
        self.__nombre = nombre

    def delNombre(self):
        del self.__nombre
    nombre = property(getNombre, setNombre, delNombre)
    # Get & Set nombre END

    # Get & Set Posición START
    def getPosicion(self):
        return self.__posicion

    def setPosicion(self, posicion:str):
        self.__posicion = posicion

    def delPosicion(self):
        del self.__posicion

    posicion = property(getPosicion, setPosicion, delPosicion)
    # Get & Set Posición END

    # Get & Set categoria START
    def getTipo(self):
        return self.__titular

    def setTipo(self, titular:bool):
        self.__titular = titular

    def delTipo(self):
        del self.__titular

    titular = property(getTipo, setTipo, delTipo)
    # Get & Set titular END

    # metodo str()
    def __str__(self):
        cadena = f"Nombre Jugador: {str(self.__nombre)}\nPosición: {str(self.__posicion)}\nJuega como: {str(self.__tipo.value)}"
        return cadena

# Instancia del objeto
j1 = Jugador("Pingüi", "Delantero", Tipo.TITULAR)
j2 = Jugador("Rulitos", "Portero", Tipo.TITULAR)
j3 = Jugador("Morado", "Capitan", Tipo.TITULAR)
j4 = Jugador("La garra", "Defensa", Tipo.TITULAR)
j5 = Jugador("Ñuqis", "Defensa", Tipo.SUPLENTE)
j6 = Jugador("Yero", "Portero", Tipo.SUPLENTE)
j7 = Jugador("Caramela", "Delantera", Tipo.SUPLENTE)


lista_jugadores = [j1, j2, j3, j4, j5, j6, j7]




class Equipo:
    def __init__(self, nombreEquipo:str, nombreEstadioEquipo:str):
        self.__nombreEquipo = nombreEquipo
        self.__nombreEstadioEquipo = nombreEstadioEquipo
        self.__jugadores = []
        self.__listaTitulares:List[self.__jugadores] = []

# Getter and Setters START
    # Get & Set nombreEquipo START
    def getNombreEquipo(self):
        return self.__nombreEquipo

    def setNombreEquipo(self, nombreEquipo:str):
        self.__nombreEquipo = nombreEquipo

    def delNombreEquipo(self):
        del self.__nombreEquipo
    nombreEquipo = property(getNombreEquipo, setNombreEquipo, delNombreEquipo)
    # Get & Set nombreEquipo END


    # Get & Set nombreEstadioEquipo START
    def getNombreEstadioEquipo(self):
        return self.__nombreEstadioEquipo

    def setNombreEstadioEquipo(self, nombreEstadioEquipo:str):
        self.__nombreEstadioEquipo = nombreEstadioEquipo

    def delNombreEstadioEquipo(self):
        del self.__nombreEstadioEquipo
    nombreEstadioEquipo = property(getNombreEstadioEquipo, setNombreEstadioEquipo, delNombreEstadioEquipo)
    # Get & Set nombreEquipo END
# Getter and Setters END

    def __str__(self):
        cadena = f"Nombre del equipo: {str(self.__nombreEquipo)}\nEstadio: {str(self.__nombreEstadioEquipo)}"
        return cadena

    def jugadores(self):
        self.__jugadores = lista_jugadores
        lista = self.__jugadores
        for j in lista:
            print(j)
            print("=====//=====//=====//=====//=====//=====")
        return j


objEquipo = Equipo("Los Toros de Manizales", "Palo Grande")
print(objEquipo.__str__())
print("-------------------------------------------")
print(objEquipo.jugadores())
