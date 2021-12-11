from chess_board_swap import Board
from time import sleep


class Solver:
    def __init__(self, board: Board) -> None:
        self.board = board

    def solve_method_A(self):
        height, width = self.board.array.shape

        for i in range(1, max(height, width)-1, 2):
            for j in range(i, 0, -1):
                if j < i / 2:
                    break
                self.board.swap_rows(j)
                self.board.swap_columns(j)
                # self.board.draw_board()

    def solve_method_B(self):
        height, width = self.board.array.shape

        for i in range(1, height-1, 2):
            for j in range(i, 0, -1):
                if j < i / 2:
                    break
                self.board.swap_rows(j)
                self.board.draw_board()

        for i in range(1, width-1, 2):
            for j in range(i, 0, -1):
                if j < i / 2:
                    break
                self.board.swap_columns(j)
                self.board.draw_board()

    def solve_method_C(self):
        self.board.draw_board()

        height, width = self.board.array.shape
        for i in range(1, max(height, width)-1, 2):
            for j in range(i, 0, -1):
                if j < i / 2:
                    break
                self.board.swap_rows(j)
                self.board.swap_columns(j)
            self.board.draw_board()
        print('done')
        self.board.draw_board()


if __name__ == '__main__':
    WIDTH, HEIGHT = 40, 40

    board = Board(WIDTH, HEIGHT)
    print(board)

    solver = Solver(board)
    solver.solve_method_B()
    print('solved')

    solver.board.draw_board()
    solver.board.renderer.screen.exitonclick()
