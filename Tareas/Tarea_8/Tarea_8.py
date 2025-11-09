import sys
from typing import List, Tuple, Optional

class LaberintoSolver:
    """
    Resuelve el laberinto cargado desde un archivo .txt con un formato tipo CSV
    usando backtracking y una pila para almacenar la ruta de la solución
    """
    def __init__(self, filename : str):
        self.maze: List[List[int]] = []
        self.rows: int = 0
        self.cols: int = 0
        self.start: Optional[Tuple[int, int]] = None
        self.end: Optional[Tuple[int, int]] = None

        self.path_stack: List[Tuple[int, int]] = []

        try:
            self._cargar_laberinto(filename)
            self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        except FileNotFoundError:
            print(f"Error en el archivo {filename}, no fue encontrado.", file=sys.stderr)
            sys.exit(1)
        except Exception as e:
            print(f"Error al cargar el laberinto {e}", file=sys.stderr)
            sys.exit(1)

    def _cargar_laberinto(self, filename : str):
        """
        Cargar el laberinto desde el archivo .txt con un formato tipo CSV
        """
        with open(filename, 'r') as f:
            self.rows = int(f.readline().strip())
            self.cols = int(f.readline().strip())

            for r in range(self.rows):
                linea = f.readline().strip().split(',')
                if len(linea) != self.cols:
                    raise ValueError(f"Error en la fila {r}: se esperaban {self.cols} columnas, pero se encontraron {len(linea)} después de separar con comas")

                if 'E' in linea:self.start = (r, linea.index('E'))
                if 'S' in linea: self.end = (r, linea.index('S'))
                self.maze.append(linea)

        if self.start is None:
            raise ValueError("No se encontró un punto de entrada 'E' en el Laberinto")
        if self.end is None:
            raise ValueError("No se encontró un punto de salida 'S' en el laberinto")


    def resolver(self):
        """
        Punto de entrada público para iniciar la solución del laberinto
        """
        if not self.start:
            print("El laberinto no se cargó correctamente (sin inicio)")
            return

        start_row, start_col = self.start
        if self._backtrack_solve(start_row, start_col):
            print("¡Solución Encontrada!")
            print("La ruta de solución (fila, columna) es:")
            self._imprimir_ruta()
        else:
            print("No se encontró una ruta de solución para este laberinto")

    def _backtrack_solve(self, r: int, c: int) -> bool:
        """
        Función recursiva con backtracking
        """
        if r < 0 or c < 0 or r >= self.rows or c >= self.cols:
            return False #Se salió del mapa
        if self.maze[r][c] == '1':
            return False #Es una pared
        if self.visited[r][c]:
            return False #Ya se había visitado esa celda

        self.visited[r][c] = True #Marca la celda en la memoria para que sepamos que ya la visitamos
        self.path_stack.append((r, c)) #Se añade a la pila porque resulta ser una solución potencial

        if self.maze[r][c] == 'S': #Se verifica que la celda sea o no sea la Salida con ''S''
            return True
        #ya que no es ''s'', entonces buscamos de nuevo en las direcciones con llamadas recursivas una y otra vez
        if self._backtrack_solve(r + 1, c): return True
        if self._backtrack_solve(r - 1, c): return True
        if self._backtrack_solve(r, c + 1): return True
        if self._backtrack_solve(r, c - 1): return True

        self.path_stack.pop() #Al llegar a este punto nos damos cuenta qué ya no hay opciones y, por lo tanto,
        #estamos en un espacio sin salida y hacemos el "Backtrack"
        return False

    def _imprimir_ruta(self):
        """
        Imprime la solución en forma de pila
        """

        maze_con_ruta = [row[:] for row in self.maze]

        for (r, c) in self.path_stack:
            if self.maze[r][c] != 'E' and self.maze[r][c] != 'S':
                maze_con_ruta[r][c] = '*'

        print("\n--- Vista de Laberinto resuelto ---")
        for row in maze_con_ruta:
            print(" ".join(row)) #añade espacios a la salida para que sea visualmente más bonito

        print(f"\n--- Coordenadas de la pila ({len(self.path_stack)} PASOS) ---")
        for i, paso in enumerate(self.path_stack):
            print(f"PASO {i}: {paso}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python Tarea_8.py <filename>")
        sys.exit(1)

    nombre_archivo = sys.argv[1]
    solver = LaberintoSolver(nombre_archivo)
    solver.resolver()