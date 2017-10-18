# Universidad Simon Bolivar
# Laboratorio de Ingenieria de Software
# Tarea 2
# Autores:
#   - Amanda Camacho   12-10644
#   - Lautaro Villalon 12-10427
# Descripcion: funcion que calcula el monto a pagar de un servicio.



class BilleteraElectronica:
  
    def __init__(self, identif, nombres, apellidos, CI, PIN):
        self.id=identif
        self.saldoInicial=0
        self.nombres=nombres
        self.apellidos=apellidos
        self.CI=CI
        self.PIN=PIN


	#######################
	#Estructura de Credito#
	#######################
    class Credito:
        # Estructura para guardar cosas relacionadas con la billetera
        def __init__(self, monto, fecha, identif):
            self.monto=monto
            self.fecha= fecha
            self.id= identif
      
    class Debito:
	#   Estructura para registrar los consumos o debitos de la billetera 
        def __init__(self, monto, fecha, identif):
		    self.monto=monto
		    self.fecha= fecha
		    self.id= identif


    ####################################
	# Funciones saldo,recarga y consumo#
	####################################
    
    def saldo(self):
		print (self.saldoInicial)
		return self.saldoInicial

    def recarga(self, monto, fecha, identif, CI):
        if CI== self.CI:
            if monto>0:
                self.Credito(monto, fecha, identif)
                self.saldoInicial= self.saldoInicial + monto
                return True
            else:
                print("El saldo no puede ser negativo")
                return False
        else:
            print("USUARIO INCORRECTO")
            return False


    
    def consumo(self, monto, fecha, identif, CI, PIN):
        if CI==self.CI and PIN==self.PIN:
            if monto<0:
                print("El monto de consumo no puede ser negativo")
                return False
            if self.saldoInicial>=monto:
                self.Debito(monto, fecha, identif)
                self.saldoInicial= self.saldoInicial - monto
                return True
            else:
                print("Saldo insuficiente")
                return False
        else:
            print("DATOS INCORRECTOS")
            return False

            