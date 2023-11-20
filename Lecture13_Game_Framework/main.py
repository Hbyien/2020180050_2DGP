from pico2d import open_canvas, delay, close_canvas
import play_mode as start_mode #컨트롤 r 하면 검색해서 모두 바꿀수 있다.
import game_framework
#import logo_mode as start_mode
#import title_mode as start_mode #title 모드를 임포트 하는데 이름은 스타트모드

open_canvas()
game_framework.run(start_mode)
close_canvas()

# logo_mode.init()
# # game loop
#
# while logo_mode.running:
#     logo_mode.handle_events()
#     logo_mode.update()
#     logo_mode.draw()`
#     delay(0.01)
#
# # finalization code
# logo_mode.finish()
# close_canvas()
