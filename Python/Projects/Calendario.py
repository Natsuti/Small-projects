import datetime, time, logging


grid_c = {"x": 98, "y": 24, "cx": 14, "cy": 4}
DAYS = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
MONTHS = (
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
)


def crear_matriz(lx, ly):
    grid = [[" " for i in range(lx + 1)] for x in range(ly + 1)]
    return grid


def mostrar(lis):
    print("\n\n\t")
    for fila in lis:
        print("\t" + "".join(fila))
    print("\n\n")


def dibujar_pixel(lis, x, y, s):
    lis[y][x] = s


def dibujar_texto(lis, x, y, s, m):
    if m == "h":
        for i in range(len(s)):
            dibujar_pixel(lis, x + i, y, s[i])
    elif m == "v":
        for i in range(len(s)):
            dibujar_pixel(lis, x, y + i, s[i])
    elif m == "d":
        for i in range(len(s)):
            dibujar_pixel(lis, x + i, y + i, s[i])


def dibujar_linea_h(lis, ix, iy, w, s):
    for column in range(w):
        dibujar_pixel(lis, ix + column, iy, s)


def dibujar_linea_v(lis, ix, iy, h, s):
    for row in range(h):
        dibujar_pixel(lis, ix, iy + row, s)


def dibujar_rectangulo(lis, x, y, w, h, s):
    dibujar_linea_v(lis, x, y, h, s)
    dibujar_linea_h(lis, x, y, w, s)
    dibujar_linea_v(lis, x + w, y, h + 1, s)
    dibujar_linea_h(lis, x, y + h, w + 1, s)


# def dibujar_grid(grid, x,y, w,h, cx,cy, s):


while True:
    for k in grid_c.keys():
        grid_c[k] = int(input(f"{k}:> "))
    grid = crear_matriz(grid_c["x"], grid_c["y"])
    dibujar_rectangulo(grid, 0, 0, grid_c["x"], grid_c["y"], "*")
    mostrar(grid)
