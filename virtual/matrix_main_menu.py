from matrix_drawing_tools import draw_figure, from_str_to_figure
from matrix_snake import Snake
from matrix_zero_cross import ZeroCross
from matrix_game_of_life import GameOfLife
from matrix_fire_effect import Fire
from matrix_minecraft_fire import MinecraftFire

class MainMenu:
    def __init__(self):
        self.gamelist = ['snake', 'zero_cross', 'game_of_life', 'fire_effect', 'minecraft_fire_effect']
        self.small_gamelist = ['sn', 'zc', 'gl', 'fe', 'mf']
        self.active_game = None
        self.status = None
        self.cursor = 0
        self.speed = 60

    def up(self):
        if self.status is None:
            self.cursor -= 1
            self.cursor %= len(self.gamelist)
        else:
            self.active_game.up()

    def down(self):
        if self.status is None:
            self.cursor += 1
            self.cursor %= len(self.gamelist)
        else:
            self.active_game.down()

    def left(self):
        if self.status is not None:
            self.active_game.left()

    def right(self):
        if self.status is not None:
            self.active_game.right()

    def click(self, matrix, framerate):
        if self.status == None:
            self.active_game = self.gamelist[self.cursor]
            self.status = 'running'
            if self.active_game == 'snake':
                self.active_game = Snake()
                return [[0 for _ in range(16)] for _ in range(16)], 2
            elif self.active_game == 'zero_cross':
                self.active_game = ZeroCross()
                return [[0 for _ in range(16)] for _ in range(16)], 60
            elif self.active_game == 'game_of_life':
                self.active_game = GameOfLife()
                return [[0 for _ in range(16)] for _ in range(16)], 10
            elif self.active_game == 'fire_effect':
                self.active_game = Fire()
                return [[0 for _ in range(16)] for _ in range(16)], 60
            elif self.active_game == 'minecraft_fire_effect':
                self.active_game = MinecraftFire()
                return [[0 for _ in range(16)] for _ in range(16)], 32
            else:
                self.status = None
                del self.active_game
                self.active_game = None
                return [[0 for _ in range(16)] for _ in range(16)], 60
        else:
            self.active_game.click(matrix)
        return matrix, framerate

    def doubleclick(self):
        if self.status is not None:
            self.status = self.active_game.doubleclick()
        else:
            del self.active_game
            self.active_game = None
            self.status = None

    def get_map(self, matrix, framerate):
        if self.status is None:
            draw_figure(0, 0, from_str_to_figure(self.small_gamelist[self.cursor]), matrix)
            return matrix, 60
        else:
            if self.active_game.name == 'snake':
                return self.active_game.get_map(matrix, framerate)
            else:
                return self.active_game.get_map(matrix, framerate)



