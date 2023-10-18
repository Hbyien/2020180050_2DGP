from pico2d import *

from grass import Grass
from grass import Grass2
from boy import Boy

import game_world


# Game object class here


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        else:
            boy.handle_event(event)


def reset_world():
    global running
    global grass
    global team
    global grass2

    global boy

    running = True

    grass = Grass()
    grass2 = Grass2()
    game_world.add_object(grass, 0)
    game_world.add_object( grass2, 2)

    boy = Boy()
    game_world.add_object(boy, 1)


def update_world():
    game_world.update()

    pass


def render_world():
    clear_canvas()
    game_world.render()
    update_canvas()


open_canvas()
reset_world()
# game loop
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)
# finalization code
close_canvas()
