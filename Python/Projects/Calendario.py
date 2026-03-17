import datetime, time, logging

logging.basicConfig(level=logging.CRITICAL, format="%(message)s")

grid_c = {"x": 99, "y": 25, "cx": 14, "cy": 4}
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
        self.capas = []

    def crear_matriz(self, w, h, s=" ", index=None):
        self.w = w
        self.h = h
        capa = [[s for _ in range(w)] for _ in range(h)]
        if index is None:
            self.capas.append(capa)
        else:
            self.capas.insert(index, capa)
        logging.debug(f"crear_matriz(): w:{self.w}, h:{self.h}")

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
            for y in self.capas[index]:
                print("\t\t" + "".join(y))
        print("\t\t\n\n")

    def pixel(self, x, y, s, index=0):
        logging.debug(f"pixel(): len(y):{len(self.capas[0])}")
        self.capas[index][y][x] = s

    def texto(self, x, y, s, m, index=0):
        if m == "v":
            for i in range(len(s)):
                logging.debug(f"texto(v): y+i:{y + i}")
                self.pixel(x, y + i, s[i], index)
        elif m == "h":
            for i in range(len(s)):
                logging.debug(f"texto(h): x+i:{x + i}")
                self.pixel(x + i, y, s[i], index)
        elif m == "d":
            for i in range(len(s)):
                logging.debug(f"texto(d): x+i:{x + i}, y+i:{y + i}")
                self.pixel(x + i, y + i, s[i], index)

    def linea(self, m, x, y, t, s, index=0):
        if m == "h":
            """h, genera lineas a los lados en las Y, si mueves Y la linea se movera arriba o abajo"""
            for column in range(t):
                logging.debug(f"linea(h): x+column:{x + column}")
                self.pixel(x + column, y, s, index)
        elif m == "v":
            """v, genera lineas a arriba abajo en las X, si mueves X la linea se movera a los lados"""
            for row in range(t):
                logging.debug(f"linea(v): y+row:{y + row}")
                self.pixel(x, y + row, s, index)
        elif m == "d":
            """va en diagonal,"""
            for i in range(t):
                logging.debug(f"linea(d): x+column:{x + i}, y+row:{y + i}")
                self.pixel(x + i, y + i, s, index)

    def rectangulo(self, x, y, w, h, s, index=0):
        logging.debug(
            f"rectangulo(): x:{x} y:{y}, h:{h}, w:{w}, x+w:{x + w}, y+h:{y + h}"
        )
        self.linea("v", x, y, h, s, index)
        self.linea("v", x + w - 1, y, h, s, index)
        self.linea("h", x, y, w, s, index)
        self.linea("h", x, y + h - 1, w, s, index)

    def grid(self, x, y, w, h, cx, cy, s, s2, index=0):
        self.rectangulo(x, y, w, h, s, index)
        for yi in range(0, h, cy):
            self.linea("h", x, yi, w, s, index)
        for xi in range(0, w, cx):
            self.linea("v", xi, y, h, s2, index)


a = Canvas()
a.crear_matriz(grid_c["x"], grid_c["y"])
a.grid(0, 0, grid_c["x"], grid_c["y"], grid_c["cx"], grid_c["cy"], "-", "|")
logging.debug(f"capas: {len(a.capas)}")
a.mostrar("c")
