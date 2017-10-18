# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#   - Amanda Camacho   12-10644
#   - Lautaro Villalon 12-10427

import unittest

from BilleteraElectronica import *

class TestSuite(unittest.TestCase):

    def testCasoInterior(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        miBilletera.recarga(5000, "04/08/2017", 111)
        miBilletera.recarga(5000, "05/08/2017", 111)

        miBilletera.consumo(9999, "15/09/2017", 2, "0000")

    def testCasoFrontera(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        miBilletera.recarga(7532, "17/10/2017", 111)

        miBilletera.consumo(3500, "17/10/2017", 121, "0000")
        miBilletera.consumo(4032, "18/10/2017", 122, "0000")

    def testCasoEsquina(self):
        miBilletera = BilleteraElectronica(1200, "Lautaro", "Villalón", "23.241.475", "0000")

        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()