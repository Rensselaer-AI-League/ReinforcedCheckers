import ai
import logic


class Game():

    def __init__(self):
        self.running = True
        self.turn = 0
        self.board = logic.Board(8, 8)
        self.input = logic.Input()
        self.output = logic.Output()
        self.ai = ai.BeginnerAI()

    def setup_ai(self):
        self.ai.OT_set_side(1)
        self.ai.OT_set_dimensions(self.board.width, self.board.heigt)

    def run(self):
        self.output.welcome()
        self.setup_ai()
        while self.running:
            self.game()

    def gamestate(self):
        gs = []
        for y in self.board.board:
            for x in y:
                gs.append(x)
        return gs

    # def game(self):
    #     self.output.to_move(self.turn)
    #     self.board.draw()

    def game(self):
        # randomly make player X or O
        self.output.to_move(self.turn)
        self.board.draw()

        if self.board.full():
            x_ct, o_ct = self.board.dominance()
            if x_ct > o_ct:
                self.output.wins("Player 1 (0)", x_ct, o_ct)
                self.ai.OT_set_winner('0')
            elif o_ct > x_ct:
                self.output.wins("Player 2 (1)", o_ct, x_ct)
                self.ai.OT_set_winner('1')
            self.board.reset()
            self.turn = '0'
            return

        legal_move = False
        while not legal_move:
            action = ''
            if self.turn == 'X':
                self.output.poll_move()
                action = self.input.prompt_move().lower()
            else:
                self.ai.OT_update_board(self.gamestate())
                action = self.ai.OT_get_move().lower()

            if action == 'f':
                self.output.player_forfeit(self.turn)
                self.board.reset()
                self.mode = "menu"
                legal_move = True
            else:
                action = list(action)
                if len(action) == 2:
                    rank = ord(action[0]) - 97
                    file = self.board.hgt - ord(action[1]) + 48
                    if self.board.place(rank, file, self.turn):
                        legal_move = True
                        if self.turn == "X":
                            self.turn = "O"
                        else:
                            self.turn = "X"

                if not legal_move:
                    self.output.illegal_move()

if __name__ == "__main__":
    g = Game()
    g.run()
