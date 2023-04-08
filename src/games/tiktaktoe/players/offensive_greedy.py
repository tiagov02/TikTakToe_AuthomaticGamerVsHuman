import random
from typing import List
from games.tiktaktoe.action import TikTakToeAction
from games.tiktaktoe.player import TikTakToePlayer
from games.state import State
from games.tiktaktoe.state import TikTakToeState


class GreedyTikTakToePlayer(TikTakToePlayer):
    CORNERS = [
        (0, 0),
        (0, 2),
        (2, 0),
        (2, 2)
    ]
    def __init__(self, player_num):
        super().__init__(f"GreedyPlayer{player_num}")
        self.player_num = player_num

    @staticmethod
    def is_first_play(state: TikTakToeState):
        for row in range(state.get_dimension()):
            for col in range(state.get_dimension()):
                if state.get_grid()[row][col] != TikTakToeState.EMPTY_CELL:
                    return False
        return True

    @classmethod
    def get_score_for_position(cls, state, position: TikTakToeAction):
        number_of_chips = 0
        grid = state.get_grid()


        for idx_row in range(state.get_num_rows()):
            if grid[idx_row][position.get_y()] == state.get_acting_player():
                number_of_chips += 1


        for idx_col in range(state.get_num_cols()):
            if grid[position.get_x()][idx_col] == state.get_acting_player():
                number_of_chips += 1


        if (position.get_x(), position.get_y(),) in cls.CORNERS:
            # verificar diagonal crescente (0,0) (1,1) (2,2)
            for idx_row, idx_col in zip(range(state.get_num_rows()), range(state.get_num_cols())):
                if grid[idx_row][idx_col] == state.get_acting_player():
                    number_of_chips += 1

            # verificar diagonal decrescente (0, 2) (1, 1) (2, 0)
            for idx_row, idx_col in zip(range(state.get_num_rows()), range(state.get_num_cols() - 1, -1, -1)):
                if grid[idx_row][idx_col] == state.get_acting_player():
                    number_of_chips += 1

        return number_of_chips

    @staticmethod
    def get_available_positions(state):
        positions = []
        grid = state.get_grid()

        for idx_row in range(state.get_num_rows()):
            for idx_col in range(state.get_num_cols()):
                if grid[idx_row][idx_col] == TikTakToeState.EMPTY_CELL:
                    positions.append(TikTakToeAction(idx_col, idx_row))

        return positions

    @classmethod
    def get_best_position_score(cls, state):
        positions = cls.get_available_positions(state)
        best_score = 0
        for position in positions:
            if cls.get_score_for_position(state, position) >= best_score:
                best_score += 1

        return best_score

    @classmethod
    def get_best_position(cls, state):
        best_score = cls.get_best_position_score(state)
        positions = cls.get_available_positions(state)
        best_positions = []
        for position in positions:
            if cls.get_score_for_position(state, position) == best_score:
                best_positions.append(position)

        return random.choice(positions)

    @classmethod
    def get_action(cls, state: TikTakToeState):
        # se for a primeira jogada
        if cls.is_first_play(state):
            corner = random.choice(cls.CORNERS)
            return TikTakToeAction(corner[0], corner[1])
        else:
            chosen_position = cls.get_best_position(state)
            state.display()
            return chosen_position

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass