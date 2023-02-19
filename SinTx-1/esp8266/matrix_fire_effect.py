from math import log
from random import getrandbits
from palettes import palletes

pallete0 = palletes[0]

LOW = (0, 14)
MEDIUM = (9, 27)
HIGH = (7, 9)
DELTA = (0, 2)


class Fire(object):
    def __init__(self, width=16, height=16, intensity=HIGH):
        self.width, self.height = width, height
        self.pixels = create()
        self.speed = 25
        self.name = 'fire_effect'
        self.cursor = 0

    def left(self):
        self.speed += 1

    def right(self):
        if self.speed != 0:
            self.speed -= 1

    def up(self):
        self.increase()

    def down(self):
        self.decrease()

    def click(self, _):
        global pallete0
        self.cursor += 1
        self.cursor %= len(palletes)
        pallete0 = palletes[self.cursor]

    def doubleclick(self):
        return None

    def update(self):
        for i in range(self.width * self.height):
            try:
                pixel_below = self.pixels[i+self.width]
                decay = int((getrandbits(12) / 4096) * 2)
                if i - decay < 0:
                    continue
                self.pixels[i - decay] = max(pixel_below - decay, 0)
            except IndexError:
                pass

    def get_map(self, matrix, _):
        return newRender(self.pixels, matrix, self.speed)

    def increase(self):
        for i in range(1, self.width + 1):
            self.pixels[-i] = min(self.pixels[-i] + myrandint(DELTA), 36)

    def decrease(self):
        for i in range(1, self.width + 1):
            self.pixels[-i] = max(self.pixels[-i] - myrandint(DELTA), 0)


def create():
    fire = [0] * 256
    for i in range(1, 17):
        fire[-i] = myrandint(HIGH)
    return fire


def myrandint(inter):
    delta = inter[1] - inter[0]
    num = getrandbits(round(log(delta, 2))) + inter[0]
    if num >= inter[1]:
        num = (inter[0] + inter[1]) // 2
    return num


def get_color(value):
        if value < len(pallete0):
            return pallete0[max(value, 0)]
        else:
            return pallete0[-1]
    

def newRender(pixels, matrix, framerate):
        newm = [[] for _ in range(16)]
        counter = 0
        for i in range(16):
            for _ in range(16):
                color = get_color(pixels[counter])
                if color != (7, 7, 7):
                    newm[i].append(color)
                else:
                    newm[i].append((0, 0, 0))
                counter += 1
        return newm, framerate