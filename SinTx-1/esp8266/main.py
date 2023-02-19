import machine, neopixel, random, time, gc, micropython
import matrix_main_menu as mmm
gc.collect()
np = neopixel.NeoPixel(machine.Pin(13), 256)
matrix = [[0 for _ in range(16)] for _ in range(16)]


@micropython.native
def convert(matrix1):
    count = 0
    matrix1 = tuple(reversed(matrix1))
    for i in range(len(matrix1)):
        if i % 2 == 0:
            for q in matrix1[i]:
                if q:
                    np[count] = (63, 63, 63)
                else:
                    np[count] = (0, 0, 0)
                count += 1
        else:
            for q in matrix1[i][::-1]:
                if q:
                    np[count] = (63, 63, 63)
                else:
                    np[count] = (0, 0, 0)
                count += 1
    np.write()


@micropython.native
def rgbConvert(matrix1):
    count = 0
    matrix1 = tuple(reversed(matrix1))
    for i in range(16):
        if i % 2 == 0:
            for q in matrix1[i]:
                np[count] = q
                count += 1
        else:
            for q in matrix1[i][::-1]:
                np[count] = q
                count += 1
    np.write()


frames_per_sec = 60
run = True
start_time = time.time_ns()
elapsed = 0
down, click, up, left, right = machine.Pin(4, machine.Pin.IN), machine.Pin(5, machine.Pin.IN), machine.Pin(14, machine.Pin.IN), machine.Pin(12, machine.Pin.IN), machine.Pin(15, machine.Pin.IN)


Main = mmm.MainMenu()
machine.freq(160000000)



while run:
    down.irq(lambda x: Main.down() if x.value() == 1 else x) #lambda x: snake.down() if x.value() == 1 else x
    up.irq(lambda x: Main.up() if x.value() == 1 else x) # lambda x: snake.up() if x.value() == 1 else x
    left.irq(lambda x: Main.left() if x.value() == 1 else x) #lambda x: snake.left() if x.value() == 1 else x
    right.irq(lambda x: Main.right() if x.value() == 1 else x) # lambda x: snake.right() if x.value() == 1 else x
    if down.value() == 1 and click.value() == 1:
        Main.doubleclick()
    elif click.value() == 1:
        matrix, frames_per_sec = Main.click(matrix, frames_per_sec)


    if Main.status is not None:
        if Main.active_game.name == 'snake':
            if Main.active_game.game:
                matrix, eated = Main.get_map(matrix, frames_per_sec)
                if eated: 
                    frames_per_sec += 0.2 
        elif 'effect' in Main.active_game.name:
            matrix, frames_per_sec = Main.get_map(matrix, frames_per_sec)
        else:
            matrix, frames_per_sec = Main.get_map(matrix, frames_per_sec)
    else:
        matrix, frames_per_sec = Main.get_map(matrix, frames_per_sec)
    if Main.status is None:
        convert(matrix)
        machine.lightsleep(int(1000 // (frames_per_sec)))
        continue
    else:
        if 'effect' not in Main.active_game.name:
            convert(matrix)
            machine.lightsleep(int(1000 // (frames_per_sec)))
            continue
        else:
            if Main.active_game.name == 'fire_effect':
                if elapsed >= frames_per_sec:
                    Main.active_game.update()
                    elapsed = 0
                elapsed += int(1000 // frames_per_sec)
            rgbConvert(matrix)
            machine.lightsleep(2)
            continue
#ampy --port COM8 rm main.py