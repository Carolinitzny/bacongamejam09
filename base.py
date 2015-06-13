class Drawable(object):
    def draw(self, surface, camera):
        pass

class Updatable(object):
    def update(self, dt):
        pass

class MouseClickListener(object):
    def onMouseClick(self, button, position):
        pass          

class KeyboardListener(object):
    def onKeyPressed(self, key, unicode):
        pass