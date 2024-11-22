from graphics import *
from cell import Cell
def main():
    win= Window(800, 600)
    celda = Cell(win)
    celda.has_left_wall= False
    celda.draw(50, 50, 100, 100)

    celda= Cell(win)
    celda.has_right_wall= False
    celda.draw(150,150,200,200)

    celda= Cell(win)
    celda.has_top_wall= False
    celda.draw(225,225,200,200)

    celda= Cell(win)
    celda.has_bottom_wall= False
    celda.draw(300,300, 500,500)


    win.wait_for_close()

main()