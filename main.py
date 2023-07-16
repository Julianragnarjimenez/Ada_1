nombre = input("Ingresa tu nombre: ")
print("¡Bienvenido,", nombre, "!")
import readchar

while True:
    tecla = readchar.readkey()
    print("Tecla presionada:", tecla)
    
    if tecla == '\x1b[A':
        break
def borrar_terminal(numero):
    os.system('cls' if os.name == 'nt' else 'clear')  # Borrar la terminal según el sistema operativo
    print("Nuevo número:", numero)

numero = 0

while True:
    tecla = readchar.readkey()
    
    if tecla == 'n':
        numero += 1
        borrar_terminal(numero)
    
    if numero >= 50:
        break
    
