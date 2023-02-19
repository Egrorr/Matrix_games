class MinecraftFire:
    def __init__(self):
        self.path1 = 'flameS/flame/'
        self.path2 = 'flameS/soul_flame/'
        self.txtname = 'matrix_pixel_flame_'
        self.ext = '.txt'
        self.name = 'minecraft_fire_effect'
        self.counter = 0
        self.speed = 16
        self.active_path = self.path1

    def left(self):
        if self.speed != 0:
            self.speed -= 1

    def right(self):
        self.speed += 1

    def up(self):
        pass

    def down(self):
        pass

    def click(self, _):
        if self.active_path == self.path1:
            self.active_path = self.path2
        else:
            self.active_path = self.path1

    def doubleclick(self):
        return None

    def get_map(self, *args):
        del args
        matrix = file_opening(self.counter, self.active_path, self.txtname)
        self.counter += 1
        self.counter %= 32
        return matrix, self.speed


def file_opening(indx, path, txtname):
    with open(f'{path}{txtname}{indx}.txt') as f:
        return [eval(f.readline()) for _ in range(16)]