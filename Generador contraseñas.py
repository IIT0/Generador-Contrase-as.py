import random
import time 
#Se inicia el programa aquí
def inicioprograma():
    print("Este programa te genera contraseñas seguras.")
    time.sleep(1)
    print("Creado por Illán Iglesias Torres")
    print("*******************************")

# Ahora se van a definir las variables de las letras, números y símbolos para que la contraseña los contenga.
letras = "abcdefghijklmnñopqrstuvwxyz"
mayúsculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
símbolos = "!/()=?ª!$%&"
números = "123456789"
conjunto = letras + mayúsculas + símbolos + números

#Se llama ahora a la función inicioprograma para que nos introduzca como funciona el programa.

inicioprograma()

#Aquí se obtienen datos del usuario acerca del número de caracteres y contraseñas quiere.
	
tamaño_contraseña = int(input("¿Cuántos caracteres quieres que tenga tu contraseña? "))
número_contraseñas = int(input("¿Cuántas contraseñas quieres generar? " ))

for x in range (0,número_contraseñas) :
    contraseña = ""
    for x in range (tamaño_contraseña) :
        caracteres_contraseña = random.choice(conjunto)
        contraseña = contraseña + caracteres_contraseña 
    print("Tu contraseña es: ", contraseña)



def finprograma():
    print("*******************************")    
    print("Gracias por utilizar este programa.")

finprograma()
	
exit





