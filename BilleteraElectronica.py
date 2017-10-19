# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#   - Amanda Camacho   12-10644
#   - Lautaro Villalon 12-10427
# Descripcion: funcion que calcula el monto a pagar de un servicio.

# -*- coding: utf-8 -*-

class BilleteraElectronica:

    def __init__(self, identif, nombres, apellidos, CI, PIN):
        self.id=identif
        self.nombres=nombres
        self.apellidos=apellidos
        self.CI=CI
        self.PIN=PIN

        self.creditos = self.Creditos()
        self.debitos = self.Debitos()

    #######################
    #Estructura de Credito#
    #######################
    class Creditos:
        # Estructura para guardar cosas relacionadas con la billetera
        def __init__(self):
            self.creditos = []

        def agregarCredito(self, monto, fecha, identif):
            self.creditos.append([monto, fecha, identif])
            return True

        def calcularTotal(self):
            total = 0

            if (len(self.creditos) == 0):
                return total

            for credit in self.creditos:
                total += credit[0]

            return total

      
    class Debitos:
    #   Estructura para registrar los consumos o debitos de la billetera 
        def __init__(self):
            self.debitos = []
#######################
    #Estructura de Credito#
    #######################
    class Creditos:
        # Estructura para guardar cosas relacionadas con la billetera
        def __init__(self):
            self.creditos = []

        def agregarCredito(self, monto, fecha, identif):
            self.creditos.append([monto, fecha, identif])
            return True

        def calcularTotal(self):
            total = 0

            if (len(self.creditos) == 0):
                return total

            for credit in self.creditos:
                total += credit[0]

            return total

      
    class Debitos:
    #   Estructura para registrar los consumos o debitos de la billetera 
        def __init__(self):
            self.debitos = []


        def agregarDebito(self, monto, fecha, identif):
            self.debitos.append([monto, fecha, identif])
            return True

        def calcularTotal(self):
            total = 0

            if (len(self.debitos) == 0):
                return total

            for debit in self.debitos:
                total += debit[0]

            return total

        def agregarDebito(self, monto, fecha, identif):
            self.debitos.append([monto, fecha, identif])
            return True

        def calcularTotal(self):
            total = 0

            if (len(self.debitos) == 0):
                return total

            for debit in self.debitos:
                total += debit[0]

            return total

    ####################################
    # Funciones saldo,recarga y consumo#
    ####################################
    
    def saldo(self):
        saldo = self.creditos.calcularTotal() - self.debitos.calcularTotal()

        return saldo

    def recarga(self, monto, fecha, identif):

        try:
            assert(monto>0)
        except:
            print("No se puede recargar un monto nulo o negativo.")
            return False


        self.creditos.agregarCredito(monto, fecha, identif)
        return True
              
    def consumo(self, monto, fecha, identif, PIN):

        try:
            assert(PIN==self.PIN)

        except:
            print("DATOS INCORRECTOS")
            return False

        if monto<0:
            print("El monto de consumo no puede ser negativo")
            return False

        if self.saldo() >= monto:
            self.debitos.agregarDebito(monto, fecha, identif)
            return True
        else:
            print("Saldo insuficiente")
            return False


            