from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
x, y = 0, 90  
shape = 'square' 

while True:
    if shape == 'square':
        while x < 800:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x += 2
            delay(0.01)
        
        while y < 600:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y += 2
            delay(0.01)
        
        while x > 0:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            x -= 2
            delay(0.01)
        
        while y > 90:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(x, y)
            y -= 2
            delay(0.01)
        
        shape = 'circle'  

    elif shape == 'circle':
        cx, cy = 400, 300  
        radius = 200 
        angle = 0

        while angle < 360:
            clear_canvas_now()
            grass.draw_now(400, 30)
            character.draw_now(cx + radius * math.cos(angle * math.pi / 180), cy + radius * math.sin(angle * math.pi / 180))
            angle += 2
            delay(0.01)

        shape = 'square'  

close_canvas()
