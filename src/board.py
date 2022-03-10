from src.cell import Cell
from random import randint
import turtle


class Board:
    def __init__(self, canvas, grid_size=600, cell_number=100):
        self._cell_number = cell_number
        self._grid_size = grid_size
        self._pen = turtle.RawTurtle(canvas)
        self._grid = [[Cell() for column_cells in range(cell_number)] for row_cells in range(cell_number)]
        self._set_pen()
        self._generate_cells()

    # configuramos el lapiz
    def _set_pen(self):
        self._pen.penup()
        self._pen.turtlesize(self._grid_size / self._cell_number / 20, self._grid_size / self._cell_number / 20)
        self._pen.shape('square')
        self._pen.color('white')
        self._pen.speed(0)
        self._pen.hideturtle()

    # generar celulas random
    def _generate_cells(self):
        for row in self._grid:
            for column in row:
                chance_number = randint(0, 9)
                if chance_number == 1:
                    column.set_alive()

    # matar a todas las celulas
    def _kill_cells(self):
        for row in self._grid:
            for column in row:
                column.set_dead()

    # generamos una celula en la posicion indicada
    def _draw_cell(self, x, y):
        self._pen.goto(x, y)
        self._pen.stamp()

    # dibujamos todas las celulas vivas
    def draw_cells(self):
        self._pen.clearstamps()

        for i in range(self._cell_number):
            for j in range(self._cell_number):
                if self._grid[i][j].is_alive():
                    cell_size = self._grid_size / self._cell_number
                    x = (cell_size * i) - (self._grid_size / 2) + (cell_size / 2)
                    y = (cell_size * j) - (self._grid_size / 2) + (cell_size / 2)
                    self._draw_cell(x, y)

    # dibujamos una linea de la cuadricula
    def _draw_line(self, x1, y1, x2, y2):  # this function draw a line between x1,y1 and x2,y2
        turtle.up()
        turtle.goto(x1, y1)
        turtle.down()
        turtle.goto(x2, y2)

    # dibujar toda la cuadricula
    def draw_grid(self):  # this function draws nxn grid
        turtle.pencolor('gray')
        turtle.pensize(1)
        turtle.hideturtle()
        half_grid = self._grid_size / 2
        cell_size = self._grid_size / self._cell_number

        x = (-half_grid)
        for i in range(self._cell_number + 1):
            self._draw_line(x, (-half_grid), x, half_grid)
            x += cell_size
        y = (-half_grid)
        for i in range(self._cell_number + 1):
            self._draw_line((-half_grid), y, half_grid, y)
            y += cell_size

    # calcular la siguiente generacion de celulas
    def update_board(self):
        living_cells = []
        dead_cells = []

        for row in range(self._cell_number):
            for column in range(self._cell_number):
                cell = self._grid[row][column]
                if self.cell_is_alive(row, column):
                    living_cells.append(cell)
                else:
                    dead_cells.append(cell)

        for cell in living_cells:
            cell.set_alive()

        for cell in dead_cells:
            cell.set_dead()

    # buscamos que celulas deben morir y cuales revivir
    def cell_is_alive(self, row, column):
        living_neighbors = 0
        cell_status = self._grid[row][column].is_alive()

        def in_grid(x, y):
            return -1 < x < self._cell_number and -1 < y < self._cell_number

        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if in_grid(row + i, column + j) and self._grid[row + i][column + j].is_alive():
                        living_neighbors += 1

        if cell_status and 1 < living_neighbors < 4:
            return True
        elif not cell_status and living_neighbors == 3:
            return True
        else:
            return False

    # matamos a todas la celulas y generamos nuevas
    def reset(self):
        self._kill_cells()
        self._generate_cells()
        self.draw_cells()

