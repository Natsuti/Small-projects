import time
import logging
import termios
import tty
import sys
import select


class Scene:
    def __init__(self, canvas):
        self.canvas = canvas
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
            for behavior in i.behaviors:
                behavior(i, self)

    def draw(self):
        pixels = []
        for s in self.sprites:
            for p in s.generar_shapes():
                pixels.append(p)
        pixels.sort(key=lambda p: p.z)
        for p in pixels:
            self.canvas.escribir_pixels(pixels)

    def render(self):
        self.canvas.mostrar("c")

    def clear(self):
        print("\033[H")
