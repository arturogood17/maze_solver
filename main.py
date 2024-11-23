from graphics import *
from cell import Cell
def main():
    win= Window(800, 600)
    celda = Cell(win)
    celda.has_right_wall= False
    celda.draw(50, 50, 100, 100)

    celda1= Cell(win)
    celda1.has_left_wall= False
    celda1.has_bottom_wall= False
    celda1.draw(100,50,150,100)

    celda.draw_move(celda1)

    celda2= Cell(win)
    celda2.has_top_wall= False
    celda2.has_right_wall= False
    celda2.draw(100,100,150, 150)

    celda1.draw_move(celda2)

    celda3= Cell(win)
    celda3.has_left_wall= False
    celda3.draw(150,100, 200,150)

    celda2.draw_move(celda3, True)


    win.wait_for_close()

main()