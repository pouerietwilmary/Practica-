
#Definir una clase Cliente que almacene un código de cliente, cedula, nombre, direccion y fecha Nacimiento.  En la clase Cliente definir una variable de clase de tipo lista que almacene todos los clientes que tienen suspendidas sus cuentas de ahorro.  Imprimir por pantalla todos los datos de clientes y el estado que se encuentra su cuenta de ahorro.
dinero = 800
clases = []
class cliente:
    def __init__(self):
        self.codigo=int(input("Digite su codigo de seguridad:\n "))
        clases.append(self.codigo)
        self.cedula=int(input("Digite su numero de cedula:\n "))
        clases.append(self.cedula)
        self.nombre=input("Digite su nombre completo:\n ")
        clases.append(self.nombre)
        self.dirrecion=input("Digite su direccion de casa:\n ")
        clases.append(self.dirrecion)
        self.fecha=int(input("Digite su fecha de nacimiento:\n "))
        clases.append(self.fecha)
class clase(cliente):
    def __init__(self):
        super().__init__()
        self.sueldo=float(input("¿Que cantidad desea retirar de su cuenta?: "))
    def dinero_retirado(self):
        if self.sueldo > dinero:
            print(clases)
            print(f"Haz sobre pasado la cantidad de dinero{self.nombre}. \nSu cuenta queda suspendida. ")
        else:
            print(f"Todavia te queda dinero para gastar. \n Pase buenas{self.nombre}.")
 

cliente1=clase()
cliente1.dinero_retirado()



