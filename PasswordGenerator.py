#Código para generar contraseñas seguras en base a la longitud deseada
import random as rnd
generador="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;':,./<>?"
password_final=""
print("Genrador de contraseñas seguras")
while True: 
    numero=int(input("Ingrese el tamaño de su contraseña: (Debe ser mayor o igual a 8 caracteres) \n"))
    if numero>=8:
        for i in range (numero):
            password=rnd.choice(generador)
            password_final+=password
        print(f"Tu contraseña segura es: {password_final}")
        break
    else:
        print("Tu contraseña debe ser de longitud 8 o más caracteres, valida eso. ")
        continue

