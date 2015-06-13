class Drawable(object):
    def draw(self, surface):
        pass

class Updateable(object):
    def update(self, dt):
        pass

class MouseClickListener(object):
    def onMouseClick(self, button, position):
        pass          

class KeyboardListener(object):
    def onKeyPressed(self, key, unicode):
        pass