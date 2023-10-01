from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1000, 800
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
mouse = load_image('hand_arrow.png')

def handle_events():
    global running
    global x, y
    global xy_list
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        # elif event.type == SDL_MOUSEBUTTONDOWN:
        #     mouse.draw(x,y)
        elif event.type == SDL_MOUSEBUTTONDOWN:
            print("hello")
            xy_list.append((x,y))
            xy_list.append((1, 2))
    pass


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
xy_list = []

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    events = get_events()
    #character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    mouse.draw(x,y)

    events = get_events()
    # for event in events:
    #     if event.type == SDL_MOUSEBUTTONDOWN:
    #         print("hello")

    handle_events()
    update_canvas()
    #frame = (frame + 1) % 8
    for i, (x, y) in enumerate(xy_list):
        print(f"{i + 1}번째 (x, y) 쌍: ({x}, {y})")


close_canvas()