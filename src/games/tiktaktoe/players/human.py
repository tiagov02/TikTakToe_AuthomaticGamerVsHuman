from games.tiktaktoe.action import TikTakToeAction
from games.tiktaktoe.player import TikTakToePlayer
from games.tiktaktoe.state import TikTakToeState


class HumanTikTakToePlayer(TikTakToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TikTakToeState):
        state.display()
        while True:
            # noinspection PyBroadException
            try:
                return TikTakToeAction(int(input(f"Player {state.get_acting_player()}, choose a line: ")),int(input(f"AND A COLUMN: ")))
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: TikTakToeState):
        # ignore
        pass

    def event_end_game(self, final_state: TikTakToeState):
        # ignore
        pass
