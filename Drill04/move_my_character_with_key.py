from pico2d import *


open_canvas()
TUK_WIDTH, TUK_HEIGHT = 1100, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')

character = load_image('animation_girl.png')


def handle_events():
    global running, dir, wir

    # fill here
    global x, y, bottom

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        # fill here
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 5
                bottom = 100
            elif event.key == SDLK_LEFT:
                dir -= 5
                bottom = 200
            elif event.key == SDLK_UP:
                wir += 5
                bottom = 0
            elif event.key == SDLK_DOWN:
                wir -= 5
                bottom = 300
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 5
            elif event.key == SDLK_LEFT:
                dir += 5
            elif event.key == SDLK_UP:
                wir -= 5
            elif event.key == SDLK_DOWN:
                wir += 5


running = True
x = TUK_WIDTH // 2
y = TUK_HEIGHT//2
frame = 0
dir = 0
wir = 0
bottom = 100

# fill here
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, bottom, 100, 100, x, y)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    y += wir * 5
    delay(0.05)
    if x <= 10:
        x = 10
    elif x >= TUK_WIDTH - 10:
        x = TUK_WIDTH -10
    elif y <= 10:
        y = 10
    elif y >= TUK_HEIGHT -10:
        y = TUK_HEIGHT - 10
close_canvas()

