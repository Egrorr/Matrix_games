import random
from matrix_drawing_tools import from_str_to_figure, draw_figure


class GameOfLife:
    def __init__(self):
        self.status = 'inmenu'
        self.cursor = (0, 0)
        self.menu_cursor = 0
        self.name = 'game_of_life'
        self.counter = 0
        self.counter2 = 0
        self.game_type = 'Rd'
        self.game_types = ['Rd', 'Ma']
        self.ended_matrix = [[0 for _ in range(16)] for _ in range(16)]

    def left(self):
        if self.status != 'inmenu':
            self.cursor = ((self.cursor[0] - 1) % 16, self.cursor[1])

    def right(self):
        if self.status != 'inmenu':
            self.cursor = ((self.cursor[0] + 1) % 16, self.cursor[1])

    def down(self):
        if self.status != 'inmenu':
            self.cursor = (self.cursor[0], (self.cursor[1] + 1) % 16)
        else:
            self.menu_cursor -= 1
            self.menu_cursor %= 2

    def up(self):
        if self.status != 'inmenu':
            self.cursor = (self.cursor[0], (self.cursor[1] - 1) % 16)
        else:
            self.menu_cursor += 1
            self.menu_cursor %= 2

    def click(self, _):
        if self.status == 'editing':
            if self.ended_matrix[self.cursor[1]][self.cursor[0]] == 0:
                self.ended_matrix[self.cursor[1]][self.cursor[0]] = 1
            else:
                self.ended_matrix[self.cursor[1]][self.cursor[0]] = 0
        elif self.status in ('pause', 'run'):
            if self.counter % 2 == 0:
                self.status = 'pause'
            else:
                self.status = 'run'
            self.counter += 1
        else:
            self.game_type = self.game_types[self.menu_cursor]
            if self.game_type == 'Rd':
                self.ended_matrix = [[random.getrandbits(1) for _ in range(16)] for _ in range(16)]
                self.status = 'run'
            elif self.game_type == 'Ma':
                self.ended_matrix = [[0 for _ in range(16)] for _ in range(16)]
                self.status = 'editing'

    def doubleclick(self):
        if self.status == 'editing':
            self.status = 'run'
            return 'running'
        else:
            return None

    def near(self, pos, matrix, system=[[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]):
        count = 0
        for i in system:
            if matrix[(pos[0] + i[0]) % len(matrix)][(pos[1] + i[1]) % len(matrix[0])]:
                count += 1
        return count

    def get_map(self, matrix, framerate):
        neww = [[0 for _ in range(16)] for _ in range(16)]
        if self.status == 'inmenu':
            draw_figure(0, 0, from_str_to_figure(self.game_types[self.menu_cursor]), matrix)

        elif self.status == 'editing':
            for i in range(16):
                for q in range(16):
                    if (q, i) == self.cursor:
                        neww[i][q] = 1
                    else:
                        neww[i][q] = self.ended_matrix[i][q]
            return neww
        elif self.status == 'run':
            if self.game_type == 'Rd' and self.counter2 == 0:
                matrix = self.ended_matrix
                self.counter2 += 1
            for i in range(16):
                for j in range(16):
                    k = self.near([i, j], matrix)
                    if matrix[i][j]:
                        if k not in (2, 3):
                            neww[i][j] = 0
                        else:
                            neww[i][j] = 1
                    elif k == 3:
                        neww[i][j] = 1
                    else:
                        neww[i][j] = 0
            return neww, framerate
        return matrix, framerate


