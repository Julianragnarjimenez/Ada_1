import os
import readchar
import random
from functools import reduce

class Juego:
    def __init__(self, mapa, start, end):
        self.mapa = mapa
        self.start = start
        self.end = end
        self.px, self.py = start

    def clear_terminal(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_map(self):
        self.clear_terminal()
        for row in self.mapa:
            print(''.join(row))

    def game_loop(self):
        while (self.px, self.py) != self.end:
            self.display_map()
            key = readchar.readkey()
            if key == '\x1b[A':  # Tecla de flecha arriba
                new_px, new_py = self.px - 1, self.py
            elif key == '\x1b[B':  # Tecla de flecha abajo
                new_px, new_py = self.px + 1, self.py
            elif key == '\x1b[C':  # Tecla de flecha derecha
                new_px, new_py = self.px, self.py + 1
            elif key == '\x1b[D':  # Tecla de flecha izquierda
                new_px, new_py = self.px, self.py - 1
            else:
                continue

            if (
                0 <= new_px < len(self.mapa) and
                0 <= new_py < len(self.mapa[0]) and
                self.mapa[new_px][new_py] != "#"
            ):
                self.mapa[self.px][self.py] = "."
                self.px, self.py = new_px, new_py
                self.mapa[self.px][self.py] = "P"

class JuegoArchivo(Juego):
    def __init__(self, map_file):
        mapa, start, end = self.parse_map_file(map_file)
        super().__init__(mapa, start, end)

    def parse_map(self, map_string):
        # Usar la función map para convertir cada línea en una lista de caracteres
        map_matrix = list(map(list, map_string.strip().split('\n')))
        return map_matrix

    def parse_map_file(self, map_file):
        with open(map_file, 'r') as f:
            lines = f.readlines()

        # Usar reduce para concatenar todas las filas leídas en una sola cadena
        map_string = reduce(lambda x, y: x + y, lines[3:], "").strip()

        dimensions = lines[0].strip().split(',')
        rows, cols = int(dimensions[0]), int(dimensions[1])
        start = tuple(map(int, lines[1].strip().split(',')))
        end = tuple(map(int, lines[2].strip().split(',')))

        # Usar la función parse_map para convertir la cadena en una matriz
        mapa = self.parse_map(map_string)

        return mapa, start, end

def main():
    map_files_folder = "maps_folder"  # Ruta de la carpeta con archivos de mapas
    map_files = os.listdir(map_files_folder)

    if not map_files:
        print("No se encontraron archivos de mapas en la carpeta.")
        return

    map_file = random.choice(map_files)
    map_file = os.path.join(map_files_folder, map_file)

    juego = JuegoArchivo(map_file)
    juego.game_loop()

if __name__ == "__main__":
    main()

