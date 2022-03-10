from src.board import Board
import turtle
import tkinter


def main():
    # creamos la pantalla
    wn = turtle.Screen()
    wn.title("Game of life")
    wn.bgcolor("black")
    wn.setup(width=800, height=650)
    wn.tracer(0)

    # creamos el tablero
    game_of_life_board = Board(wn)

    # dibujamos la grilla
    game_of_life_board.draw_grid()

    # dibujamos la primer generacion de celulas
    game_of_life_board.draw_cells()

    canvas = wn.getcanvas()

    def exit():
        wn.bye()

    # boton para resetear las celulas
    button = tkinter.Button(canvas.master, text='Reset', command=game_of_life_board.reset)
    canvas.create_window(330, -280, window=button)
    button_exit = tkinter.Button(canvas.master, text='Exit', command=exit)
    canvas.create_window(330, -240, window=button_exit)

    while True:
        wn.update()

        # creamos la proxima generacion de celulas
        game_of_life_board.update_board()
        game_of_life_board.draw_cells()


main()
