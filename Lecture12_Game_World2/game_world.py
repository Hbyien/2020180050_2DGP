objects = []

def add_objects(o):
    objects.append(o)

def update():
    for o in objects:
        o.update()


def render():
    for o in objects:
        o.draw()