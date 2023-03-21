class TikTakToeAction:
    """
    a connect 4 action is simple - it only takes the value of the column to play
    """
    __x: int
    __y: int

    def __init__(self, x: int,y:int):
        self.__x = x
        self.__y = y
        #teste

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y
