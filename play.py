import random

from board import Board, XMark, OMark, BoardUpdateError, BoardVictory, BoardStalemate


class InvalidMove(BaseException):
    pass


def run_game():
    print 'running TicTacToe!'
    board = Board()
    current_player = XMark

    while True:
        board.render()

        try:
            player_turn(board, current_player)

            if current_player == XMark:
                current_player = OMark
            else:
                current_player = XMark
        except InvalidMove as e:
            print e.message
        except BoardVictory:
            print "you won"
            board.render()
            break
        except BoardStalemate:
            print "you stalemated"
            board.render()
            break


def player_turn(board, mark):

    if mark == XMark:
        # SUPER COMPUTER TIME
        while True:
            x, y = random.randint(0,2), random.randint(0,2)

            try:
                board.update_board(x, y, mark)
                break
            except BoardUpdateError:
                pass
    else:
        player_input = raw_input()

        try:
            cleaned_input = [
                int(s.strip())
                for s in player_input.split(',')
            ]
        except:
            raise InvalidMove("Incorrect format. Please specify your turn as x, y")

        try:
            [x, y] = cleaned_input
        except ValueError:
            raise InvalidMove("Please specify two coordinates only")
        if not 0 <= x <= 2:
            raise InvalidMove("x coordinate is too large or small. Please specify a number between 0 and 2")
        if not 0 <= y <= 2:
            raise InvalidMove("y coordinate is too large or small. Please specify a number between 0 and 2")

        try:
            board.update_board(x, y, mark)
        except BoardUpdateError:
            raise InvalidMove("That location is already taken. Please choose another")


if __name__ == '__main__':
    run_game()