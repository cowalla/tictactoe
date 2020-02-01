import copy


EmptyMark = ' '
XMark = 'X'
OMark = 'O'


BOARD_LINE_FORMAT = ' %s | %s | %s '


class BoardUpdateError(BaseException):
    pass


class BoardVictory(BaseException):
    pass


class BoardStalemate(BaseException):
    pass


class Board(object):
    def __init__(self):
        self.game_state = [
            [EmptyMark, EmptyMark, EmptyMark],
            [EmptyMark, EmptyMark, EmptyMark],
            [EmptyMark, EmptyMark, EmptyMark],
        ]

    def render(self):
        for line in self.game_state:
            print BOARD_LINE_FORMAT % tuple(line)


    def update_board(self, x, y, mark):
        coordinate_value = self.game_state[x][y]

        if coordinate_value != EmptyMark:
            raise BoardUpdateError('Board position already occupied')
        else:
            self.game_state[x][y] = mark

        if self.is_victory():
            raise BoardVictory('You win!')
        elif self.is_stalemate():
            raise BoardStalemate('You stalemated!')


    def _get_victory_permutations(self):
        victory_permutations = copy.copy(self.game_state)
        victory_permutations += [
            list(v)
            for v in zip(*self.game_state)
        ]
        victory_permutations += [
            [self.game_state[0][0], self.game_state[1][1], self.game_state[2][2]],
            [self.game_state[2][0], self.game_state[1][1], self.game_state[0][2]]
        ]

        return victory_permutations


    def is_victory(self):
        victory_permutations = self._get_victory_permutations()

        for victory_condition in victory_permutations:
            items_on_line = set(victory_condition)

            if len(items_on_line) == 1 and EmptyMark not in items_on_line:
                return True

        return False

    def is_stalemate(self):
        for row in self.game_state:
            if EmptyMark in row:
                return False

        return True
