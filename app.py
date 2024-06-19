import csv
# el programa deberá calcular el ganador de votos validos considerando que los siguientes datos son proporcionados:
# region,provincia,distrito,dni,candidato,esvalido
# Si hay un candidato con >50% de votos válidos retornar un array con un string con el nombre del ganador
# Si no hay un candidato que cumpla la condicion anterior, retornar un array con los dos candidatos que pasan a segunda vuelta
# Si ambos empatan con 50% de los votos se retorna el que apareció primero en el archivo
# el DNI debe ser valido (8 digitos) ------ DONE

class Datos:
    def __init__(self, data):
        self.data = data

    def leerdatos(self, archivo):
        with open(archivo, 'r') as csvfile:
            next(csvfile)
            datareader = csv.reader(csvfile)
            for fila in datareader:
                self.data.append(fila)

class CalculaGanador:
    def __init__(self):
        self.votosxcandidato = {}

    # Separacion/Division de métodos: contarVotos, calcularGanador, calcularGanadorTotal

    def contarVotos(self, data): # Simplificacion de condicionales
        for fila in data:
            candidato = fila[4]
            esvalido = fila[5] == '1'
            dni = fila[3]

            if candidato not in self.votosxcandidato:
                self.votosxcandidato[candidato] = 0

            if esvalido and self.dniValido(dni): # Se renombraron variables (antes es_valido: ahora esValido, usando camelCase)
                self.votosxcandidato[candidato] += 1

    # Funcion que calcula el ganador de las elecciones
    def calcularGanador(self, data):
        total_votos_validos = sum(self.votosxcandidato.values())
        if total_votos_validos == 0:
            return []

        porcentaje_ganador = 0.5 * total_votos_validos
        ganador = None
        empate = []

        for candidato, votos in self.votosxcandidato.items():
            if votos > porcentaje_ganador:
                ganador = candidato
            elif votos == porcentaje_ganador:
                empate.append(candidato)

        if ganador:
            return [ganador]
        elif empate:
            return [empate[0]]
        else:
            candidatos_ord_votos = dict(sorted(self.votosxcandidato.items(), key=lambda x: x[1], reverse=True))
            return list(candidatos_ord_votos.keys())[:2]
        
    #Funcion que llama a los contarVotos y el Ganador 
    def calcularGanadorTotal(self, data): # Simplificacion de condicionales
        self.contarVotos(data)
        return self.calcularGanador(data)

    # Funcion que valida si un DNI es valido
    def dniValido(self, dni):
        return len(dni) == 8 and dni.isdigit() # Determina si el DNI tiene 8 digitos y si este es un numero
    
