from pico2d import *
import random

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def draw_mouse_point(x, y):
    mouse.draw(x, y)





running = True
a, b = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    x, y = a, b
    a = random.uniform(0, TUK_WIDTH)
    b = random.uniform(0, TUK_HEIGHT)
    dir = 100
    for i in range(0, 100, 5):
        clear_canvas()
        TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

        draw_mouse_point(a, b)
        t = i /100
        x1 = (1 - t)*x + t*a
        y1 = (1 - t)*y + t*b
        if (a-x)>0:
            dir =100
        elif (a-x <0):
            dir= 0

        character.clip_draw(frame * 100, dir, 100, 100, x1, y1)

        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.05)
    delay(0.05)





close_canvas()




