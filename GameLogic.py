
class Checker:
    def__init__(self, color, x, y, king=False):
        self.color = color
        self.x = x
        self.y = y
        self.king = king


class Board:
    def __init__(self):
        self.width = 8
        self.height = 8
        self.reset()
        self.board = [['.' for x in range(self.width)] for y in
                      range(self.height)]

        if self.height % 2 == 0:
            for i in range(self.height/2 - 1):
                for j in range(self.width):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            self.board[i][j] = Checker('red', j, i)
                            self.board[self.height-i][j] =
                            Checker('black', j, i)
                    else:
                        if j % 2 == 1:
                            self.board[i][j] = Checker('red', j, i)
                            self.board[self.height-i][j] =
                            Checker('black', j, i)
        else:
            for i in range(self.height/2):
                for j in range(self.width):
                    if i % 2 == 0:
                        if j % 2 == 0:
                            self.board[i][j] = Checker('red', j, i)
                            self.board[self.height-i][j] =
                            Checker('black', j, i)
                    else:
                        if j % 2 == 1:
                            self.board[i][j] = Checker('red', j, i)
                            self.board[self.height-i][j] =
                            Checker('black', j, i)

    def reset(self):
        self.board = [['.' for x in range(self.width)] for y in
                      range(self.height)]

    def in_bounds(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return False
        else:
            return True

    def is_occupied(self, x, y):
        if self.in_bounds(x, y):
            return self.board[y][x]
        else:
            return False

    def set(self, x, y, color):
        self.board[y][x] = color

    # def valid_move(self, x_old, y_old, x_new, y_new):
    #     if self.in_bounds(x_old, y_old) and self.in_bounds(x_new, y_new)
    # and abs(x_new - x_old) <= 2 and abs(y_new - y_old) <=2:
    #         if is_occupied(x_new, y_new) == False:
    #             if abs(x_new - x_old) == 1 and abs(y_new - y_old) == 1:
    #                 self.set(self, x_old, y_old, x_new, y_new)
    #                 self.set()
    #         else if is_occupied(x_new,y_new) != is_occupied(x_old, y_old):
    #     else:
    #         return False
    #     if abs(x_new - x_old) == 1 and in_bounds(x_old, y_old)
    # in_bounds(x_new, y_new):
    #         if abs(y_new - y_old) == 1 and in_bounds(x_old, y_old)
    # in_bounds(x_new, y_new):


class Input:
    def prompt_move(self, msg=''):
        return raw_input(msg)

    def prompt_menu(self, msg=''):
        return raw_input(msg)


class Output:
    def welcome(self):
        print "Welcome to Reinforced Checkers"

    def to_move(self, turn):
        print turn.upper() + "'s move:"

    def poll_move(self):
        print "Where do you want to move"

    def illegal_move(self):
        print "That move is illegal"

    def player_forfeits(self, turn):
        print "scrub"

    def menu(self):
        print "h ...... help/tutorial"
        print "g ...... start game"
        print "a ...... start game vs ai"
        print "q ...... quit"

    def controls(self):
        print "f - scrub"
        print "a5 b6 - moves piece from a5 to b6"

    print tutorial(self):
        print "... literally checkers...."

    def wins(self, winner):
        print winner, " is not a scrub."
