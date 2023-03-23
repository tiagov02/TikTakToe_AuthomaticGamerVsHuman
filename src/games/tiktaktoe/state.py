from typing import Optional

from games.tiktaktoe.action import TikTakToeAction
from games.tiktaktoe.result import TikTakToeResult
from games.state import State


class TikTakToeState(State):
    EMPTY_CELL = -1

    def __init__(self, dimension: int = 6):
        super().__init__()

        if dimension < 3:
            raise Exception("the number of rows must be 4 or over")
        """
        the dimensions of the board
        """
        self.__dimension = dimension

        """
        the grid
        """
        self.__grid = [[TikTakToeState.EMPTY_CELL for _i in range(self.__dimension)] for _j in range(self.__dimension)]

        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False

    def __check_winner(self, player):
        internal_result = True
        external_result = True
        # check for 4 across --> line
        for row in range(0, self.__dimension):
            for col in range(0, self.__dimension):
                internal_result = self.__grid[row][col] == player
                external_result = internal_result == external_result


        if not external_result:
            # check for 4 up and down --> column
            for col in range(0, self.__dimension):
                for row in range(0, self.__dimension):
                    internal_result = self.__grid[row][col] == player
                    external_result = internal_result == external_result

        # check upward diagonal
        for row in range(3, self.__dimension):
            for col in range(0, self.__dimension - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row - 1][col + 1] == player and \
                        self.__grid[row - 2][col + 2] == player and \
                        self.__grid[row - 3][col + 3] == player:
                    return True

        # check downward diagonal
        for row in range(0, self.__dimension - 3):
            for col in range(0, self.__dimension - 3):
                if self.__grid[row][col] == player and \
                        self.__grid[row + 1][col + 1] == player and \
                        self.__grid[row + 2][col + 2] == player and \
                        self.__grid[row + 3][col + 3] == player:
                    return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: TikTakToeAction) -> bool:
        x = action.get_x()
        y = action.get_y()

        # valid column
        if x < 0 or x >= self.__dimension or y < 0 or y >= self.__dimension:
            return False

        # full column
        if self.__grid[x][y] != TikTakToeState.EMPTY_CELL:
            return False

        return True

    def update(self, action: TikTakToeAction):
        x = action.get_x()
        y = action.get_y()

        # drop the checker
        if self.__grid[x][y] == self.EMPTY_CELL:
            self.__grid[x][y] = self.__acting_player

        # determine if there is a winner
        self.__has_winner = self.__check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1

    def __display_cell(self, row, col):
        print({
                  0: 'O',
                  1: 'X',
                  TikTakToeState.EMPTY_CELL: ' '
              }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        for col in range(0, self.__dimension):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        for col in range(0, self.__dimension):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__dimension):
            print('|', end="")
            for col in range(0, self.__dimension):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    def __is_full(self):
        return self.__turns_count > (self.__dimension * self.__dimension)

    def is_finished(self) -> bool:
        return self.__has_winner or self.__is_full()

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = TikTakToeState(self.__dimension)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__dimension):
            for col in range(0, self.__dimension):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[TikTakToeResult]:
        if self.__has_winner:
            return TikTakToeResult.LOOSE if pos == self.__acting_player else TikTakToeResult.WIN
        if self.__is_full():
            return TikTakToeResult.DRAW
        return None

    def get_dimension(self):
        return self.__dimension

    def before_results(self):
        pass

    def get_possible_actions(self):
        return list(filter(
            lambda action: self.validate_action(action),
            map(
                lambda x,y: TikTakToeAction(x,y),
                range(0, self.get_dimension()))
        ))

    def sim_play(self, action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
