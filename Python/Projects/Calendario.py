import datetime, time, logging

logging.basicConfig(level=logging.CRITICAL, format="%(message)s")

grid_c = {"x": 98, "y": 29, "cx": 14, "cy": 4}
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


class Canvas:
    def __init__(self, w=98, h=24):
        self.w = w
        self.h = h

    def crear_matriz(self, w, h, capas=1):
        self.w = w
        self.h = h
        self.capas = [[[" " for i in range(w)] for x in range(h)] for i in range(capas)]
        logging.debug(f"crear_matriz(): w:{self.w}, h:{self.h}")

    def mostrar(self):
        print("\n\n\t\t")
        for y in self.capas[0]:
            print("\t\t" + "".join(y))
        print("\t\t\n\n")

    def pixel(self, x, y, s):
        logging.debug(f"pixel(): len(y):{len(self.capas[0])}")
        self.capas[0][y][x] = s

    def texto(self, x, y, s, m):
        if m == "v":
            for i in range(len(s)):
                logging.debug(f"texto(v): y+i:{y + i}")
                self.pixel(x, y + i, s[i])
        elif m == "h":
            for i in range(len(s)):
                logging.debug(f"texto(h): x+i:{x + i}")
                self.pixel(x + i, y, s[i])
        elif m == "d":
            for i in range(len(s)):
                logging.debug(f"texto(d): x+i:{x + i}, y+i:{y + i}")
                self.pixel(x + i, y + i, s[i])

    def linea(self, m, x, y, t, s):
        if m == "h":
            """h, genera lineas a los lados en las Y, si mueves Y la linea se movera arriba o abajo"""
            for column in range(t):
                logging.debug(f"linea(h): x+column:{x + column}")
                self.pixel(x + column, y, s)
        elif m == "v":
            """v, genera lineas a arriba abajo en las X, si mueves X la linea se movera a los lados"""
            for row in range(t):
                logging.debug(f"linea(v): y+row:{y + row}")
                self.pixel(x, y + row, s)
        elif m == "d":
            """va en diagonal,"""
            for i in range(t):
                logging.debug(f"linea(d): x+column:{x + i}, y+row:{y + i}")
                self.pixel(x + i, y + i, s)

    def rectangulo(self, x, y, w, h, s):
        logging.debug(
            f"rectangulo(): x:{x} y:{y}, h:{h}, w:{w}, x+w:{x + w}, y+h:{y + h}"
        )
        self.linea("v", x, y, h, s)
        self.linea("v", x + w - 1, y, h, s)
        self.linea("h", x, y, w, s)
        self.linea("h", x, y + h - 1, w, s)


a = Canvas()
"""while True:
    for k in grid_c.keys():
        grid_c[k] = int(input(f"{k}:> "))"""


a.crear_matriz(grid_c["x"], grid_c["y"])
a.rectangulo(0, 0, grid_c["x"], grid_c["y"], "*")
for y in range(0, grid_c["y"], grid_c["cy"]):
    a.linea("h", 0, y, grid_c["x"], "*")
for x in range(0, grid_c["x"], grid_c["cx"]):
    a.linea("v", x, 0, grid_c["y"], "*")
a.mostrar()
