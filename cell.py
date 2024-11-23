from graphics import Line, Point
class Cell:
    def __init__(self, win= None):
        self.has_left_wall= True
        self.has_right_wall= True
        self.has_top_wall= True
        self.has_bottom_wall= True
        self.__x1= None
        self.__y1= None
        self.__x2= None
        self.__y2= None
        self.__win = win
    
    def draw(self, x1, y1, x2, y2):
        if self.__win is None:
            return
        self.__x1= x1
        self.__y1= y1
        self.__x2= x2
        self.__y2= y2
        if self.has_left_wall:
            line= Line(Point(self.__x1, self.__y1), Point(self.__x1, self.__y2))
            self.__win.draw_line(line)
        if self.has_right_wall:
            line= Line(Point(self.__x2, self.__y1), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)
        if self.has_top_wall:
            line= Line(Point(self.__x1, self.__y1), Point(self.__x2, self.__y1))
            self.__win.draw_line(line)
        if self.has_bottom_wall:
            line= Line(Point(self.__x1, self.__y2), Point(self.__x2, self.__y2))
            self.__win.draw_line(line)

    def draw_move(self, to_cell, undo= False):
        half_lenght = abs(self.__x2 - self.__x1) //2
        x_center = half_lenght + self.__x1
        y_center = half_lenght +  self.__y1

        half_lenght2= abs(to_cell.__x2 - to_cell.__x1) //2
        x_center2 = half_lenght2 + to_cell.__x1
        y_center2 = half_lenght2 +  to_cell.__y1

        fill_color = "red"

        if undo:
            fill_color= "gray"

        line= Line(Point(x_center, y_center), Point(x_center2, y_center2))
        self.__win.draw_line(line, fill_color)
        
        
