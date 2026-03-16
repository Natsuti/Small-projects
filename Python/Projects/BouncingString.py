import time
import logging

logging.basicConfig(level=logging.CRITICAL, format="%(message)s")
x, y, dx, dy, tx, ty = 2, 2, 1, 1, 100, 20


def dibujar(x, y, s):
    print(f"\033[{y};{x}H{s}", end="")


def limpiar():
    print("\033[2J", end="")


def dibujar_bitmap(x, y, b):
    for i, linea in enumerate(b):
        print(f"\033[{y+i};{x}H{linea}", end="")
        logging.debug(f"{i}")


a = [
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
]
while True:
    limpiar()
    dibujar_bitmap(x, y, a)
    x += dx
    y += dy

    if x <= 1 or x >= tx:
        dx *= -1

    if y <= 1 or y >= ty:
        dy *= -1

    time.sleep(0.1)
