from pico2d import load_image

class Idle:

    @staticmethod  # do(self) 이렇게 쓰지 않아도 됨  / 필요한 함수만 모아놨다 / 객체 생성용이 아니라 함수를 모아두는 용도로 변경
    def do():
        print('IDLE do')
        pass

    @staticmethod
    def enter():
        print('IDLE Entered')
        pass


    @staticmethod
    def exit():
        print('IDLE Exit')
        pass

    @staticmethod
    def draw():
        pass


class StateMachine:

    def __init__(self):
        self.cur_state = Idle #클래스는 객체생성이 아니고 함수를 모아두는 용도가 있기 때문에 Idle이란 그룹을 가리키는 것이다.
        pass
    def start(self):
        self.cur_state.enter()
        pass

    def update(self):
        self.cur_state.do()
        pass
    def draw(self):
        pass




class Boy:
    def __init__(self):
        self.x, self.y = 400, 90
        self.frame = 0
        self.dir = 0
        self.action = 3
        self.image = load_image('animation_sheet.png')
        self.state_machine = StateMachine()
        self.state_machine.start()

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.state_machine.update()

    def handle_event(self, event):
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 100, self.action * 100, 100, 100, self.x, self.y)
        self.state_machine.draw()
