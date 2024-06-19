# refactor-practice
## Practica de refactor

Integrantes: 
- Flavia Mañuico
- Yamileth Rincón

# Técnicas Aplicadas
## Separación/División de Métodos

- Técnica: División de la funcionalidad en métodos específicos: contarVotos, calcularGanador, calcularGanadorTotal.
- Descripción: Mejora la organización del código al dividir la lógica en funciones más pequeñas y específicas, facilitando su comprensión, mantenimiento y reutilización.
- Beneficio: Mejora la claridad y modularidad del código, permitiendo pruebas y depuración más fáciles.

```py
def contarVotos(self, data):

def calcularGanador(self, data):

def calcularGanadorTotal(self, data):
```

## Simplificación de Condicionales

- Técnica: Simplificación de condicionales para mejorar la legibilidad.
- Descripción: Se utilizan condicionales simplificados para determinar si un voto es válido, reduciendo la complejidad de la lógica dentro de las estructuras condicionales.
- Beneficio: Mejora la legibilidad del código y reduce posibles errores al simplificar la lógica.

```py
candidatos_ord_votos = dict(sorted(self.votosxcandidato.items(), key=lambda x: x[1], reverse=True))
return list(candidatos_ord_votos.keys())[:2]

    
return len(dni) == 8 and dni.isdigit()
```

## Validación de Datos

- Técnica: Creación de un método para validar datos (dniValido).
- Descripción: Este método encapsula la lógica para verificar si el DNI es válido (longitud y si es numérico), centralizando la validación en un solo lugar.
- Beneficio: Facilita la actualización de la lógica de validación y asegura que se aplique de manera consistente en todo el código.

```py
def dniValido(self, dni):
    return len(dni) == 8 and dni.isdigit()
```

## Renombrado de Variables

- Técnica: Uso de nombres de variables descriptivos (cambio de es_valido a esValido usando camelCase).
- Descripción: Renombrar variables para hacerlas más significativas y consistentes con las convenciones de nomenclatura, facilita la lectura y comprensión del código.
- Beneficio: Aumenta la claridad y mantiene la coherencia en el estilo de código.

```py
# Antes
es_valido = fila[5] == '1'

# Después
esvalido = fila[5] == '1'
```

## Uso de Diccionario para Conteo

- Técnica: Utilización de un diccionario (self.votosxcandidato) para contar los votos por candidato.
- Descripción: Se utiliza un diccionario para mapear cada candidato a su número de votos, lo que permite un acceso rápido y eficiente para incrementar el conteo de votos y evaluar los resultados.
- Beneficio: Simplifica el manejo de datos al proporcionar una estructura clara y eficiente para contar y recuperar votos por candidato.

```py
def contarVotos(self, data): # Simplificacion de condicionales
        for fila in data:
            candidato = fila[4]
            esvalido = fila[5] == '1'
            dni = fila[3]

            if candidato not in self.votosxcandidato:
                self.votosxcandidato[candidato] = 0

            if esvalido and self.dniValido(dni): # Se renombraron variables (antes es_valido: ahora esValido, usando camelCase)
                self.votosxcandidato[candidato] += 1
```

## Uso de variables globales
- Técnica: Generar una variable global en la clase para su uso posterior en funciones oredeterminadas que la llamen.

- Descripción: En este caso se utilizará al diccionario votosxcandidato = {} en varias funciones para el cálculo de ganaros, empate y segunda vuelta de forma eficiente.

- Beneficio: Simplifica el manejo de las variables sin tener que realizar llamadas repetitivas y aplicar funciones para mejorar la claridad del algoritmo.

```py
def __init__(self):
    self.votosxcandidato = {}
```

## Ordenamiento de Datos para Segunda Vuelta

- Técnica: Ordenamiento de candidatos por votos para determinar los candidatos para la segunda vuelta.
- Descripción: Ordena el diccionario de candidatos y sus votos en orden descendente para identificar los dos candidatos con más votos en caso de no haber un ganador claro.
- Beneficio: Permite una evaluación ordenada y eficiente de los resultados para determinar la necesidad de una segunda vuelta.

```py
else:
    candidatos_ord_votos = dict(sorted(self.votosxcandidato.items(), key=lambda x: x[1], reverse=True))
    return list(candidatos_ord_votos.keys())[:2]
```