import pygame as pg
import matrix_main_menu as mmm


pg.init()
clock = pg.time.Clock()
x, y = 100, 100
NUM_OF_CELLS = 16
size = [512, 512]
minilen = size[0] // NUM_OF_CELLS
screen = pg.display.set_mode(size)
pg.display.set_caption('SinTx-1')
screen.fill((0, 0, 0))
run = True
frames_per_sec = 60
matrix = [[0 for _ in range(16)] for _ in range(16)]
elapsed = 0
print()
print('Space: play/pause/draw/delete/change palette')
print('End: exit/end active game mode')
print('Up: up/increase effect')
print('Down: down/decrease effect')
print('Right: right/speed up')
print('Left: left/speed down')
print()

Main = mmm.MainMenu()


pg.display.flip()
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                Main.left()
            elif event.key == pg.K_RIGHT:
                Main.right()
            elif event.key == pg.K_DOWN:
                Main.down()
            elif event.key == pg.K_UP:
                Main.up()
            elif event.key == pg.K_SPACE:
                matrix, frames_per_sec = Main.click(matrix, frames_per_sec)
            elif event.key == pg.K_END:
                Main.doubleclick()

    if Main.status is not None:
        if Main.active_game.name == 'snake':
            if Main.active_game.game:
                matrix, eated = Main.get_map(matrix, frames_per_sec)
                if eated:
                    frames_per_sec += 0.2
        elif Main.active_game.name == 'fire_effect':
            if elapsed >= frames_per_sec:
                Main.active_game.update()
                elapsed = 0
            elapsed += clock.tick(frames_per_sec)
            matrix, frames_per_sec = Main.get_map(matrix, frames_per_sec)
        else:
            matrix, frames_per_sec = Main.get_map(matrix, frames_per_sec)
    else:
        matrix, frames_per_sec = Main.get_map(matrix, frames_per_sec)
                 
    pg.display.set_caption(f'{Main.active_game.name.capitalize() if Main.status is not None else "Menu"}    {int(clock.get_fps())}')
    for i in range(0, size[0], minilen):
        for q in range(0, size[1], minilen):
            if matrix[i // minilen][q // minilen] == 1:
                pg.draw.rect(screen, (255, 255, 255), (q, i, minilen, minilen)) 
            elif matrix[i // minilen][q // minilen] == 0:
                pg.draw.rect(screen, (0, 0, 0), (q, i, minilen, minilen))
            else:
                pg.draw.rect(screen, matrix[i // minilen][q // minilen], (q, i, minilen, minilen))
    pg.display.flip()
    clock.tick(frames_per_sec)
pg.quit()