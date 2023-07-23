import os
import readchar

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def create_maze_matrix(maze_str):
    # Convertir el laberinto en una matriz de caracteres
    maze_matrix = [list(row) for row in maze_str.strip().split("\n")]

    # Completar los dos caracteres de paredes faltantes al final
    for row in maze_matrix:
        row.append("#")
    maze_matrix.append(["#" for _ in range(len(maze_matrix[0]))])

    return maze_matrix

def show_maze(maze):
    clear_screen()
    for row in maze:
        print("".join(row))

def main_loop(maze, start, end):
    px, py = start  # Coordenadas del jugador al inicio, que es la posición inicial.

    while (px, py) != end:
        show_maze(maze)
        key = readchar.readkey()

        if key == 'n':
            number += 1
            if number > 50:
                number = 50
            clear_screen()
            print(f"Tecla presionada: {key}")
            print(f"Número: {number}")
        elif key == readchar.key.UP:
            new_px, new_py = px - 1, py
        elif key == readchar.key.DOWN:
            new_px, new_py = px + 1, py
        elif key == readchar.key.LEFT:
            new_px, new_py = px, py - 1
        elif key == readchar.key.RIGHT:
            new_px, new_py = px, py + 1
        else:
            continue

        if 0 <= new_px < len(maze) and 0 <= new_py < len(maze[0]) and maze[new_px][new_py] != "#":
            maze[px][py] = "."
            px, py = new_px, new_py
            maze[px][py] = "P"

def main():
    print("¡Bienvenido al juego de laberinto!")
    player_name = input("Por favor, ingresa tu nombre: ")
    print(f"¡Hola, {player_name}! Comencemos a jugar.")

    maze_str = """
    #######
    #...D#
    #.#.#.#
    #.#.#.#
    #...D#
    #######
    """

    start = (1, 1)
    end = (4, 4)

    maze = create_maze_matrix(maze_str)
    main_loop(maze, start, end)

if __name__ == "__main__":
    main()
