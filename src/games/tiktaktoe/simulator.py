from games.tiktaktoe.player import TikTakToePlayer
from games.tiktaktoe.state import TikTakToeState
from games.game_simulator import GameSimulator


class TikTakToeSimulator(GameSimulator):

    def __init__(self, player1: TikTakToePlayer, player2: TikTakToePlayer, num_rows: int = 6, num_cols: int = 7):
        super(TikTakToeSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the tiktaktoe grid
        """
        self.__num_rows = num_rows
        self.__num_cols = num_cols

    def init_game(self):
        return TikTakToeState(self.__num_rows, self.__num_cols)

    def before_end_game(self, state: TikTakToeState):
        # ignored for this simulator
        pass

    def end_game(self, state: TikTakToeState):
        # ignored for this simulator
        pass
