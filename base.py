class Drawable(object):
    def draw(self, surface, camera):
        pass

class Updatable(object):
    def update(self, dt):
        pass

class Mortal(object):
    def __init__(self):
        self.alive = True

    def die(self):
        self.alive = False

class MouseClickListener(object):
    def onMouseClick(self, button, position):
        pass

class KeyboardListener(object):
    def onKeyPressed(self, key, unicode):
        pass
