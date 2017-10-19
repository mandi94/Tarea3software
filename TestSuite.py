# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#   - Amanda Camacho   12-10644
#   - Lautaro Villalon 12-10427

import unittest

from BilleteraElectronica import *

class TestSuite(unittest.TestCase):

    # Caso Interior: Probamos una recarga de 10000 y un consumo de 9999.
    def testCasoInterior(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        miBilletera.recarga(5000, "04/08/2017", 111)
        miBilletera.recarga(5000, "05/08/2017", 111)

        miBilletera.consumo(9999, "15/09/2017", 2, "0000")

    # Caso Frontera: Probamos una recarga de 7532 y un consumo de 7532.
    def testCasoFrontera(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        miBilletera.recarga(7532, "17/10/2017", 111)

        miBilletera.consumo(3500, "17/10/2017", 121, "0000")
        miBilletera.consumo(4032, "18/10/2017", 122, "0000")

    # Caso Esquina: Probamos un consumo mayor al saldo. Recarga de 5000 y consumo de 5001. 
    def testCasoEsquina(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        miBilletera.recarga(5000, "04/08/2017", 111)

        miBilletera.consumo(5001, "05/08/2017", 121, "0000")

    # Caso Esquina 1: Probamos una recarga negativa y un consumo con PIN erroneo.
    def testCasoEsquina1(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        miBilletera.recarga(-3456, "10/05/2017", 121)

        miBilletera.consumo(4000, "11/05/2017", 131, "1234")

    # Malicia: Probamos un PIN erroneo.
    def testMalicia(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalon", "23.241.475", "0000")

        miBilletera.recarga(7321, "05/09/2017", 111)

        miBilletera.consumo(7321, "06/09/2017", 121, "1234")

    # Malicia 1: Probamos una recarga negativa.
    def testMalicia1(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalon", "23.241.475", "0000")

        miBilletera.recarga(-5, "08/10/2017", 111)

    # Malicia 2: Probamos un consumo negativo.
    def testMalicia2(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalon", "23.241.475", "0000")

        miBilletera.consumo(-5, "08/10/2017", 111, "0000")




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()