import pygame

"""
Example usage:

    import effects, pygame
    img = pygame.image.load('some-image.png')

    # tints the image red
    red_img = effects.apply(img, effects.Multiply([255, 0, 0]))

"""

class _MathOp(object):
    def __init__(self, color):
        self.color = list(color)
        while len(self.color) < 4:
            self.color.append(255)

    def __call__(self, color, *_):
        return tuple(min(255, max(0, self.op(a, b))) for a, b in zip(color, self.color))

class Multiply(_MathOp):
    def op(self, a, b):
        return a * b / 255

class Add(_MathOp):
    def op(self, a, b):
        return a + b

class Fade(object):
    def __init__(self, alpha):
        self.alpha = alpha

    def __call__(self, color, *_):
        return (color[0], color[1], color[2], int(color[3] * self.alpha))


def apply(img, kernel):
    """applies the kernel (function of signature: color, image, x, y) to every pixel of the surface"""
    img = img.copy()
    img.lock()

    for x in range(img.get_width()):
        for y in range(img.get_height()):
            p = (x, y)
            c = img.get_at(p)
            c = kernel(c, img, x, y)
            img.set_at(p, c)

    img.unlock()
    return img