import unittest

from app import CalculaGanador, Datos
        
class TestCalculaGanador(unittest.TestCase):

    def setUp(self):
        self.calculadora = CalculaGanador()

    def test_archivo(self): 
        datos = Datos([])
        datos.leerdatos('0204.csv')
        self.assertEqual(self.calculadora.calcularGanadorTotal(datos.data), ['Dennis Reyna', 'Aundrea Grace'])

    def test_dniInvalido(self):
        datatest = [
        ['Áncash', 'Asunción', 'Acochaca', '408100', 'Eddie Hinesley', '1'], # Este es el dni que es invalido
        ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.assertEqual(self.calculadora.calcularGanadorTotal(datatest), ['Aundrea Grace'])

    def test_calcularganador(self):
        datatest = [
        ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
        ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
        ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.assertEqual(self.calculadora.calcularGanadorTotal(datatest), ['Aundrea Grace'])

    def test_empate(self):
        datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1']
        ]
        self.assertEqual(self.calculadora.calcularGanadorTotal(datatest), ['Eddie Hinesley'])

    def test_segundaVuelta(self):
        datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Dennis Reyna', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Dennis Reyna', '1'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Dennis Reyna', '1']
        ]
        self.assertEqual(self.calculadora.calcularGanadorTotal(datatest), ['Aundrea Grace', 'Dennis Reyna'])

    def test_votos_invalidos(self):
        datatest = [
            ['Áncash', 'Asunción', 'Acochaca', '40810062', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '57533597', 'Eddie Hinesley', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '86777322', 'Aundrea Grace', '0'],
            ['Áncash', 'Asunción', 'Acochaca', '23017965', 'Aundrea Grace', '0']
        ]
        self.assertEqual(self.calculadora.calcularGanadorTotal(datatest), [])

    def test_sin_votos_validos(self):
        datatest = []
        self.assertEqual(self.calculadora.calcularGanadorTotal(datatest), [])
    

if __name__ == '__main__':
    unittest.main()
