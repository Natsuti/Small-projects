from .Pixel import Pixel


class Texto:
    def __init__(self, x, y, simbolo, m):
        self.simbolo = simbolo
        self.m = m
        self.x = x
        self.y = y
        self.w = max([len(s) for s in simbolo])
        self.h = 1

    def generar(self):
        if self.m == "h":
            for s in range(len(self.simbolo)):
                yield Pixel(self.x + s, self.y, None, None, self.simbolo[s])
        elif self.m == "v":
            for s in range(len(self.simbolo)):
                yield Pixel(self.x, self.y + s, None, None, self.simbolo[s])
        elif self.m == "d":
            for s in range(len(self.simbolo)):
                yield Pixel(self.x + s, self.y + s, None, None, self.simbolo[s])
        elif self.m == "di":
            for s in range(len(self.simbolo)):
                yield Pixel(self.x - s, self.y - s, None, None, self.simbolo[s])


class Linea:
    def __init__(self, x, y, largo, simbolo, m):
        self.x = x
        self.y = y
        self.largo = largo
        self.simbolo = simbolo
        self.m = m

    def generar(self):
        if self.m == "h":
            for i in range(self.largo + 1):
                yield Pixel(self.x + i, self.y, None, None, self.simbolo)
        elif self.m == "v":
            for i in range(self.largo + 1):
                yield Pixel(self.x, self.y + i, None, None, self.simbolo)
        elif self.m == "d":
            for i in range(self.largo + 1):
                yield Pixel(self.x + i, self.y + i, None, None, self.simbolo)
        elif self.m == "di":
            for i in range(self.largo + 1):
                yield Pixel(self.x + i, self.y - i, None, None, self.simbolo)


class Rectangulo:
    def __init__(self, x, y, w, h, simbolo1, simbolo2):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.simbolo1 = simbolo1
        self.simbolo2 = simbolo2

    def generar(self):
        lados = [
            Linea(self.x, self.y, self.h, self.simbolo1, "v"),
            Linea(self.x, self.y, self.w, self.simbolo2, "h"),
            Linea(self.w + self.x, self.y, self.h, self.simbolo1, "v"),
            Linea(self.x, self.y + self.h, self.w, self.simbolo2, "h"),
        ]
        for lado in lados:
            yield from lado.generar()


class Bitmap:
    def __init__(self, data):
        self.data = data
        self.w = max(len(row) for row in self.data)
        self.h = len(self.data)

    def generar(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                yield Pixel(x, y, None, None, self.data[y][x])
