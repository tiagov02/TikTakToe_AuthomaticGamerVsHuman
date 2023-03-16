from random import randint

from games.tiktaktoe.action import TikTakToeAction
from games.tiktaktoe.player import TikTakToePlayer
from games.tiktaktoe.state import TikTakToeState
from games.state import State


class RandomTikTakToePlayer(TikTakToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TikTakToeState):
        return TikTakToeAction(randint(0, state.get_num_cols()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
