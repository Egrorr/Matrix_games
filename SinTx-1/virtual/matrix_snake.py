import random

class Snake:
    def __init__(self):
        self.head = (8, 8)
        self.move_direction = (1, 0)
        self.food_list = []
        self.counter = 0
        self.game = True
        self.paused = True
        self.count1 = 0
        self.name = 'snake'
        self.eaten_food = 0
        self.snake = [(6, 8), (7, 8), (8, 8)]

    def left(self):
        if self.move_direction != (1, 0):
            self.move_direction = (-1, 0)
            
    def right(self):
        if self.move_direction != (-1, 0):
            self.move_direction = (1, 0)
            
    def up(self):
        if self.move_direction != (0, 1):
            self.move_direction = (0, -1)
            
    def down(self):
        if self.move_direction != (0, -1):
            self.move_direction = (0, 1)
            
    def click(self, _):
        self.pause()
    
    def doubleclick(self):
        return None
        
    def get_map(self, matrix, framerate):
        self.judge()
        eated = 0
        if self.game and self.paused:
            self.head = (self.head[0] + self.move_direction[0], self.head[1] + self.move_direction[1])
            eated = self.eat(framerate)
            if not eated:
                self.snake = self.snake[1:] + [self.head]
            else:
                self.snake.append(self.head)

            if self.counter != 0 and self.counter % 20 == 0:
                self.spawn_food()
            self.draw_on_matrix(matrix)
            self.counter += 1
        elif self.paused and not self.game:
            matrix = self.game_over(matrix)
        return (matrix, eated)
                    
    def pause(self):
        self.paused = False if self.count1 % 2 == 0 else True
        self.count1 += 1

    def eat(self, framerate):
        if self.head not in self.food_list:
            return False
        else: 
            del self.food_list[self.food_list.index(self.head)]
            self.eaten_food += 1
            return framerate + 0.1
    
    def spawn_food(self):
        k = False
        while not k:
            x = random.getrandbits(4)
            y = random.getrandbits(4)
            if (x, y) not in self.snake and (x, y) not in self.food_list:
                self.food_list.append((x, y))
                k = True

    def draw_on_matrix(self, matrix):
        for i in range(len(matrix)):
            for q in range(len(matrix[i])):
                if (q, i) in self.snake or (q, i) in self.food_list:
                    matrix[i][q] = 1
                else: 
                    matrix[i][q] = 0
        return matrix

    def judge(self):
        if len(self.snake) != len(set(self.snake)):
            self.game = False
        if len(list(filter(lambda x: 0 <= x[0] <= 15 and 0 <= x[1] <= 15, self.snake))) != len(self.snake):
            self.game = False

    def game_over(self, matrix):
        from matrix_drawing_tools import draw_figure, from_num_to_figure, matrix_clear
        matrix = matrix_clear(matrix)
        draw_figure(0, 0, from_num_to_figure(self.eaten_food), matrix)
        return matrix
    
    

        