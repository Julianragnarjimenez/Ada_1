nombre = input("Ingresa tu nombre: ")
print("¡Bienvenido,", nombre, "!")
import readchar

while True:
    tecla = readchar.readkey()
    print("Tecla presionada:", tecla)
    
    if tecla == '\x1b[A':
        break