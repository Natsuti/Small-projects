import time
import logging
import termios
import tty
import sys
import select
from .Renderer import Renderer


class Scene:
    def __init__(self, canvas):
        self.canvas = canvas
        self.renderer = Renderer(self.canvas)
        self.sprites = []
        self.input_state = set()

    def add_sprite(self, sprite):
        self.sprites.append(sprite)

    def leer_input(self):
        while True:
            dr, _, _ = select.select([sys.stdin], [], [], 0)
            if not dr:
                break
            key = sys.stdin.read(1)
            self.input_state.add(key)

    def update(self):
        self.input_state.clear()
        self.leer_input()
        for i in self.sprites:
            if i.behaviors is not None:
                for behavior in i.behaviors:
                    behavior(i, self)

    def draw(self):
        pixels = []
        for s in self.sprites:
            for p in s.generar_shapes():
                pixels.append(p)
        pixels.sort(key=lambda p: p.z)
        self.canvas.escribir_pixels(pixels)

    def render(self):
        self.renderer.render()

    def clear(self):
        print("\033[H")
        self.canvas.limpiar(0)

    def start(self):
        while True:
            self.clear()
            self.update()
            self.draw()
            self.render()
            time.sleep(0.016)
