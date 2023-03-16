from games.tiktaktoe.player import TikTakToePlayer
from games.tiktaktoe.state import TikTakToeState
from games.game_simulator import GameSimulator


class TikTakToeSimulator(GameSimulator):

    def __init__(self, player1: TikTakToePlayer, player2: TikTakToePlayer,dimension):
        super(TikTakToeSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the tiktaktoe grid
        """
        self.__dimension = dimension

    def init_game(self):
        return TikTakToeState(self.__dimension)

    def before_end_game(self, state: TikTakToeState):
        # ignored for this simulator
        pass

    def end_game(self, state: TikTakToeState):
        # ignored for this simulator
        pass
