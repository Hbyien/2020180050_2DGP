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
            mouse.draw(x, y)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            xy_list.append((x, y))



def draw_mouse(xy_list):
    for i, (x, y) in enumerate(xy_list):
        mouse.draw(x,y)

#def move_character(xy_list):
    # global a, b
    # global frame
    # dir = 100
    # for j, (x, y) in enumerate(xy_list):
    #     for i in range(0, 100, 5):
    #         clear_canvas()
    #         TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    #
    #         t = i / 100
    #         x1 = (1 - t) * a + t * x
    #         y1 = (1 - t) * b + t * y
    #         if (a - x) > 0:
    #             dir = 0
    #         elif (a - x < 0):
    #             dir = 100
    #         character.clip_draw(frame * 100, dir, 100, 100, x1, y1)
    #         update_canvas()
    #         frame = (frame + 1) % 8
    #         delay(0.05)
    #     a, b = x, y

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
xy_list = []
a,b = 0, 0
frame = 0
x2, y2 =0, 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)


    handle_events()
    mouse.draw(x, y)
    print(xy_list)

    update_canvas()

    dir = 100
    for j, (x2, y2) in enumerate(xy_list):

        for i in range(0, 100, 5):
            clear_canvas()
            TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
            handle_events()

            draw_mouse(xy_list)
            t = i / 100
            x1 = (1 - t) * a + t * x2
            y1 = (1 - t) * b + t * y2
            if (a - x2) > 0:
                dir = 0
            elif (a - x2 < 0):
                dir = 100
            character.clip_draw(frame * 100, dir, 100, 100, x1, y1)
            update_canvas()
            frame = (frame + 1) % 8
            delay(0.05)


        xy_list.pop(0)
        a, b = xy_list[0]
        print(xy_list)


close_canvas()
