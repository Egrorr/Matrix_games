from matrix_drawing_tools import draw_figure


class ZeroCross:
    def __init__(self):
        self.logic_matrix = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]
        self.counter = 0
        self.counter2 = 0
        self.name = 'zero_cross'
        self.cursor = (0, 0)
        self.k = False
    
    def left(self):
        self.cursor = ((self.cursor[0] - 1) % 3, self.cursor[1])

    def right(self):
        self.cursor = ((self.cursor[0] + 1) % 3, self.cursor[1])
    
    def down(self):
        self.cursor = (self.cursor[0], (self.cursor[1] + 1) % 3)
    
    def up(self):
        self.cursor = (self.cursor[0], (self.cursor[1] - 1) % 3)
    
    def click(self, matrix):
        if self.logic_matrix[self.cursor[1]][self.cursor[0]] == -1:
            if self.counter % 2 == 0:
                self.logic_matrix[self.cursor[1]][self.cursor[0]] = 1
            else:
                self.logic_matrix[self.cursor[1]][self.cursor[0]] = 0
            self.counter += 1
            if self.judgement(matrix):
                self.k = True       
    
    def doubleclick(self):
        return None

    def get_map(self, matrix, framerate):
        for i in range(len(self.logic_matrix)):
            for q in range(len(self.logic_matrix[i])):
                if self.logic_matrix[i][q] == 1 and self.cursor != (q, i) and not self.k:
                    draw_figure(q, i, 'cross', matrix)
                elif self.logic_matrix[i][q] == 1 and self.cursor == (q, i) and not self.k:
                    draw_figure(q, i, 'active_cross', matrix)
                elif self.logic_matrix[i][q] == 0 and self.cursor != (q, i) and not self.k:
                    draw_figure(q, i, 'zero', matrix)
                elif self.logic_matrix[i][q] == 0 and self.cursor == (q, i) and not self.k:
                    draw_figure(q, i, 'active_zero', matrix)
                elif self.logic_matrix[i][q] == -1 and self.cursor != (q, i) and not self.k:
                    draw_figure(q, i, 'empty_struct', matrix)
                elif self.logic_matrix[i][q] == -1 and self.cursor == (q, i) and not self.k:
                    draw_figure(q, i, 'corner', matrix)
        return matrix, framerate

    def judgement(self, matrix):
        xc = list([list([(i, q) for q in range(len(self.logic_matrix[i])) if self.logic_matrix[i][q] == 1]) for i in range(len(self.logic_matrix))])
        oc = list([list([(i, q) for q in range(len(self.logic_matrix[i])) if self.logic_matrix[i][q] == 0]) for i in range(len(self.logic_matrix))])
        xco = list([list([(q, i) for q in range(len(self.logic_matrix[i])) if self.logic_matrix[q][i] == 1]) for i in range(len(self.logic_matrix))])
        oco = list([list([(q, i) for q in range(len(self.logic_matrix[i])) if self.logic_matrix[q][i] == 0]) for i in range(len(self.logic_matrix))])
        for i in range(3):
            if len(xc[i]) == 3:
                self.win(1, f'l_{i}', matrix)
                return True
            elif len(xco[i]) == 3:
                self.win(1, f'v_{i}', matrix)
                return True
            elif len(oc[i]) == 3:
                self.win(0, f'l_{i}', matrix)
                return True
            elif len(oco[i]) == 3:
                self.win(0, f'v_{i}', matrix)
                return True
        if self.logic_matrix[0][0] == self.logic_matrix[1][1] == self.logic_matrix[2][2] != -1:
            self.win(self.logic_matrix[0][0], 'd_b', matrix)
            return True
        elif self.logic_matrix[0][2] == self.logic_matrix[1][1] == self.logic_matrix[2][0] != -1:
            self.win(self.logic_matrix[0][2], 'd_s', matrix)
            return True
        if -1 not in self.logic_matrix[0] and -1 not in self.logic_matrix[1] and -1 not in self.logic_matrix[2]:
            self.win(-1, '-1', matrix)
            return True
        return False
    
    def win(self, num, type, matrix):
        if num == 1:
            if 'l' in type:
                draw_figure(0, (5 * int(type[2])), 'hline', matrix)
            elif 'v' in type:
                draw_figure((5 * int(type[2])), 0, 'vline', matrix)
            elif type == 'd_b':
                draw_figure(0, 0, 'bdiagonal', matrix)
            else:
                draw_figure(0, 0, 'sdiagonal', matrix)
        elif num == 0:
            if 'l' in type:
                draw_figure(0, (5 * int(type[2])), 'hline', matrix)
            elif 'v' in type:
                draw_figure((5 * int(type[2])), 0, 'vline', matrix)
            elif type == 'd_b':
                draw_figure(0, 0, 'bdiagonal', matrix)
            else:
                draw_figure(0, 0, 'sdiagonal', matrix)
        else:
            draw_figure(0, 0, 'tie', matrix)

