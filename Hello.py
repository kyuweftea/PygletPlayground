from pyglet.gl import *
from Triangle import Triangle


class MyWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super(MyWindow, self).__init__(*args, **kwargs)
        glClearColor(0.149, 0.196, 0.22, 1.0)

        self.triangle = Triangle()

    def on_draw(self):
        self.clear()
        glDrawArrays(GL_TRIANGLES, 0, 3)

    def on_resize(self, width, height):
        glViewport(0, 0, width, height)


if __name__ == '__main__':
    window = MyWindow(1920, 1080, "MyWindow HAHA", fullscreen=True)
    pyglet.app.run()
