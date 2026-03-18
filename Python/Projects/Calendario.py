import datetime, time, logging

logging.basicConfig(level=logging.CRITICAL, format="%(message)s")

grid_c = {"x": 98, "y": 24, "cx": 14, "cy": 4}
DATES = {
    "DAYS": (
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
    ),
    "MONTHS": (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
}


class Sprite:
    def __init__(self, x=None, y=None, capa=None, shape=None, fondo=None):
        self.x = x
        self.y = y
        self.capa = capa
        self.shape = shape
        self.fondo = fondo
        self.w = max(len(le) for le in self.shape)
        self.h = len(self.shape)
        self.lx = self.w - 1
        self.ly = self.h - 1

    def generar(self):
        for i in range(len(self.shape)):
            for p in range(len(self.shape[i])):
                if self.fondo is None and self.shape[i][p] == " ":
                    continue
                yield {
                    "x": self.x + p,
                    "y": self.y + i,
                    "capa": self.capa,
                    "char": self.shape[i][p],
                }


class Canvas:
    def __init__(self):
        self.capas = []

    def crear_matriz(self, w, h, s=" ", index=None):
        self.w = w
        self.h = h
        capa = [[s for _ in range(w)] for _ in range(h)]
        if index is None:
            self.capas.append(capa)
        else:
            self.capas.insert(index, capa)
        self.lx = w - 1
        self.ly = h - 1

    def limpiar_matriz(self, index):
        self.capas[index] = [[None for _ in range(self.w)] for _ in range(self.h)]

    def borrar_matriz(self, index):
        if index == 0:
            return
        self.capas.pop(index)

    def mostrar(self, m="m", index=0):
        print("\n\n\t\t")
        if m == "c":
            for y in range(self.h):
                fila = ""
                for x in range(self.w):
                    pixel = " "
                    for capa in reversed(self.capas):
                        if capa[y][x] is not None:
                            pixel = capa[y][x]
                            break
                    fila += pixel
                print("\t\t" + fila)
        if m == "m":
            for fila in self.capas[index]:
                linea = ""
                for x in fila:
                    if x is not None:
                        linea += x
                print("\t\t" + linea)
        print("\t\t\n\n")

    def pixel(self, p):
        logging.debug(
            f"p.x:{p["x"]}, limite x:{self.lx}, p.y:{p["y"]}, limite y:{self.ly}"
        )
        if (p["x"] >= 0 and p["x"] <= self.lx) and (p["y"] >= 0 and p["y"] <= self.ly):
            logging.debug("s")
            if len(p["char"]) == 1:
                self.capas[p["capa"]][p["y"]][p["x"]] = p["char"]


a = Canvas()
a.crear_matriz(grid_c["x"], grid_c["y"])
# a.grid(0, 0, grid_c["x"], grid_c["y"], grid_c["cx"], grid_c["cy"], "-", "|")
logging.debug(f"capas: {len(a.capas)}")
a.crear_matriz(grid_c["x"], grid_c["y"], None, 1)
s = Sprite(
    0,
    0,
    0,
    [
        "          *",
        "         ***",
        "        *****",
        "       *******",
        "      *********",
        "     *****  ****",
        "    *****    ****",
        "   ******    *****",
        "  *****        ****",
        " ***             ***",
        "*                   *",
    ],
)
s.x, s.y = 2, 2
dx = 1
dy = 1
while True:
    print("\033[H", end="")
    a.limpiar_matriz(0)
    if s.x <= 1 or s.x + s.lx >= a.lx:
        dx *= -1
    if s.y <= 1 or s.y + s.ly >= a.ly:
        dy *= -1
    s.x += dx
    s.y += dy
    for p in s.generar():
        a.pixel(p)
    a.mostrar("c")
    time.sleep(0.1)
"""
a.mostrar("c")
"""
