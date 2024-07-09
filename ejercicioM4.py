print("Ejercicio 1 Crear una contraseña segura: ")
print()

#Definir las variables

def comprobarContrasena(password):
    largo = False
    mayus = False
    numer = False

#Utilizar condicionales
    if len(password) > 8:
        largo = True
    for i in range(len(password)):
        if password[i].isupper():
            mayus = True
        if password[i].isnumeric():
            numer = True


#Una constraseña es segura si cuenta con mayuscula y numeros

    if largo and mayus and numer:
        return True
    else:
        return False
    
#Que imprima ingresar una contraseña segura
password = input("Ingresa una contraseña segura: ")
verificacion = comprobarContrasena(password)
if verificacion:
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")


print("Ejercicio 2 Escribir un programa que lea números sin utilizar ciclos: ")
print()

def sumar_numeros():
    # Leer un número del usuario
    entrada = input("Ingrese un número (o presione espacio para finalizar): ")

    # Verificar si el usuario presionó espacio
    if entrada == ' ':
        return 0
    else:
        # Convertir la entrada a un número y llamar recursivamente a la función
        numero = int(entrada)
        return numero + sumar_numeros()

# Llamar a la función y mostrar el resultado
resultado = sumar_numeros()
print(f"La suma de los números ingresados es: {resultado}")
    


print("Ejercicio 3 Crear una clase llamada cuenta: ")
print()

class Cuenta:
    def __init__(self, num_cuenta, nom_titular, saldo_inicial, tipo_cuenta):
        # Inicializar los atributos de la cuenta
        self.num_cuenta = num_cuenta
        self.nom_titular = nom_titular
        self.saldo = saldo_inicial
        self.tipo_cuenta = tipo_cuenta

    def depositar(self, cantidad):
        # Método para realizar un depósito en la cuenta
        self.saldo += cantidad
        print(f"Depósito de ${cantidad} realizado en la cuenta {self.num_cuenta}.")

    def retirar(self, cantidad):
        # Método para realizar un retiro de la cuenta
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad} realizado en la cuenta {self.num_cuenta}.")
        else:
            print("Saldo insuficiente.")

    def obtener_balance(self):
        # Método para obtener el balance actual de la cuenta
        print(f"Balance de la cuenta {self.tipo_cuenta} de {self.nom_titular} numero {self.num_cuenta}: ${self.saldo}")


class Cajero:
    def __init__(self):
        # Crear una instancia de la clase Cuenta al inicializar el Cajero
        self.cuenta = Cuenta(num_cuenta="123456", nom_titular="Juan Perez", saldo_inicial=10, tipo_cuenta="ahorro")

    def operaciones(self):
        while True:
            print('Bienvenido a su banco')
            self.opcion = int(input('''
            ------------------------------
            Por favor, indique qué operación desea realizar:
            1. Consultar balance
            2. Depositar a cuenta
            3. Retirar efectivo
            4. Salir
            '''))

            if self.opcion == 1:
                self.cuenta.obtener_balance()
            elif self.opcion == 2:
                cantidad_deposito = int(input('Indique la cantidad que desea depositar: '))
                self.cuenta.depositar(cantidad_deposito)
            elif self.opcion == 3:
                cantidad_retiro = int(input('Indique la cantidad que desea retirar: '))
                self.cuenta.retirar(cantidad_retiro)
            elif self.opcion == 4:
                self.salir()
            else:
                print('Lo sentimos, opción no válida. Intente de nuevo.')

            continuar = input('¿Desea realizar otra operación? (s/n): ')
            if continuar.lower() != 's':
                self.salir()

    def salir(self):
        print('==========================================')
        print('Gracias por usar nuestros servicios!')
        print('==========================================')
        exit()


# Crear una instancia de Cajero y ejecutar operaciones
cajero = Cajero()
cajero.operaciones()
