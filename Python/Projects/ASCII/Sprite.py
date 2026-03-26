from .Pixel import Pixel


class Sprite:
    def __init__(
        self, x, y, z, shapes, estile=None, behaviors=None, capa=0, fondo=True
    ):
        self.x = x
        self.y = y
        self.capa = capa
        self.z = z
        self.fondo = fondo
        self.shapes = shapes
        self.w, self.h = self.bbox()
        self.estile = estile or {}
        self.dx = 1
        self.dy = 1
        self.behaviors = behaviors

    def generar_shapes(self):
        for shape in self.shapes:
            for i in shape.generar():
                if not self.fondo and i.simbolo == " ":
                    yield Pixel(
                        self.x + i.x,
                        self.y + i.y,
                        self.capa,
                        self.z,
                        i.simbolo,
                        self.estile,
                        True,
                    )
                elif self.fondo:
                    yield Pixel(
                        self.x + i.x,
                        self.y + i.y,
                        self.capa,
                        self.z,
                        i.simbolo,
                        self.estile,
                    )

    def bbox(self):
        if not self.shapes:
            return 0
        min_x = min(s.x for s in self.shapes)
        max_x = max(s.x + s.w for s in self.shapes)
        min_y = min(s.y for s in self.shapes)
        max_y = max(s.y + s.h for s in self.shapes)
        return (max_x - min_x, max_y - min_y)

    def mover_sprite(self, nx, ny):
        self.x = nx
        self.y = ny
