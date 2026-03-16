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


def dibujar(lis, x, y, s):
    lis[y][x] = s


def crear_matriz(lx, ly):
    grid = [[" " for i in range(lx + 1)] for x in range(ly + 1)]
    return grid


def crear_grid(lis, lx, ly, cx, cy):
    for y in range(ly + 1):
        for x in range(lx + 1):
            if y % cy == 0:
                dibujar(lis, x, y, "*")
            elif x % cx == 0:
                dibujar(lis, x, y, "*")


def mostrar(lis):
    print("\n\n\t")
    for fila in lis:
        print("\t" + "".join(fila))
    print("\n\n")


def crear_cosa():
    while True:
        for k in grid_c.keys():
            grid_c[k] = int(input("> "))
        grid = crear_matriz(grid_c["x"], grid_c["y"])
        crear_grid(grid, grid_c["x"], grid_c["y"], grid_c["cx"], grid_c["cy"])
        mostrar(grid)


crear_cosa()
