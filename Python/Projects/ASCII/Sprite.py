from .Pixel import Pixel


class Sprite:
    def __init__(self, x, y, z, shapes, estile, behaviors=None, capa=0, fondo=True):
        self.x = x
        self.y = y
        self.capa = capa
        self.z = z
        self.fondo = fondo
        self.shapes = shapes
        self.estile = estile
        self.w, self.h = self._calcular_bbox() or None
        self.dx = 1
        self.dy = 1
        self.behaviors = behaviors

    def generar_shapes(self):
        for shape in self.shapes:
            for i in shape.generar():
                if not self.fondo and i.simbolo == " ":
                    yield Pixel(
                        self.x + i.x, self.y + i.y, self.capa, self.z, i.simbolo, True
                    )
                elif self.fondo:
                    yield Pixel(
                        self.x + i.x, self.y + i.y, self.capa, self.z, i.simbolo
                    )

    def mover_sprite(self, nx, ny):
        self.x = nx
        self.y = ny

    def _calcular_bbox(self):
        max_w = 0
        max_h = 0
        for s in self.shapes:
            w, h = s.bbox()
            max_w = max(max_w, w)
            max_h = max(max_h, h)
        return max_w, max_h
