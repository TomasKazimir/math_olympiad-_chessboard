import numpy as np
import math
from drawing import Renderer


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.array = np.arange(width * height).reshape(height, width)
        # 0101
        # 1010 pattern
        for i, row in enumerate(self.array):
            j = 0
            for col in row:
                x = 0
                if i % 2:  # odd row
                    if j % 2:  # odd col
                        x = 1
                else:  # even row
                    if not j % 2:  # even col
                        x = 1
                self.array[i, j] = x
                j += 1
        self.screensize = (800, 800)
        self.renderer = Renderer(1, self.screensize, (0, 0))

    def __str__(self) -> str:
        return 'Board:\n' + str(self.array)

    def swap_rows(self, row_index: int):
        try:
            self.array[[row_index, row_index+1]] = \
                self.array[[row_index+1, row_index]]
        except IndexError:
            print('invalid index')

    def swap_columns(self, column_index: int):
        try:
            self.array[:, [column_index, column_index + 1]] \
                = self.array[:, [column_index + 1, column_index]]
        except IndexError:
            print('invalid index')

    def draw_board(self):
        self.renderer.clear()
        array_height, array_width = self.array.shape
        sidelength = min(
            self.screensize[0]/array_width, self.screensize[1]/array_height)
        x = -self.screensize[0] / 2
        y = self.screensize[1] / 2 + sidelength - array_height * sidelength

        self.renderer.goto(x, y - sidelength)
        self.renderer.draw_shape(((0, 0), (array_width * sidelength, 0), (array_width *
                                 sidelength, array_height*sidelength), (0, array_height * sidelength)), ['gray70', 'gray70'])

        for i, row in enumerate(self.array):
            j = 0
            for col in row:
                self.renderer.goto(x + sidelength * j, y + sidelength * i)
                if col == 1:
                    # n = 50
                    # s = sidelength * math.sin(3.1415926/n)
                    # self.renderer.draw_reg_pol(s, n, mode='outer')
                    self.renderer.draw_reg_pol(sidelength, 4)
                j += 1
                # if i < len(row) - 1:
                #     break

        self.renderer.render_frame()


if __name__ == '__main__':
    WIDTH, HEIGHT = 8, 8
    board = Board(WIDTH, HEIGHT)
    print(board)

    while 1:
        board.draw_board()
        command = input()
        try:
            if command.startswith('r'):
                board.swap_rows(int(command[1:])-1)
            elif command.startswith('c'):
                board.swap_columns(int(command[1:])-1)
        except:
            print('invalid command')
