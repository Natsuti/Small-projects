import time, logging, termios, tty, sys, select

logging.basicConfig(level=logging.CRITICAL, format="%(message)s")


class Canvas:
    """Simula una pantalla wxh, cada capa/matriz es un lienzo, cuando toca mostrar combina todos los lienzos/capas para crear una escena. Contrato: w=witdh, h=height, w,h y capas deben ser int, capas=numero de lienzos, el limite del canvas es w-1, h-1, todos los methods de canvas trabajan con Pixels y solo Pixels. Invarianza= w,h siempre int positivos, siempre debe haber aunque sea una capa(base), coordenadas siempre deben ser accedidas [y][x]/(y,x), se recorre por filas(y) no por x(lineas)"""

    def __init__(self, w, h, capas=1):
        self.w = w
        self.h = h
        self.capas = [
            [[None for _ in range(self.w)] for _ in range(self.h)] for _ in range(capas)
        ]
        self.lx = w - 1
        self.ly = h - 1

    def crear_capa(self):
        """Contrato: self.w=width y self.h=height, 1 capa por uso. Invarianza:"""
        self.capas.append([[None for _ in range(self.w)] for _ in range(self.h)])

    def limpiar(self, capa):
        """Contrato: capa=index dentro de la lista de capas self.capas, reemplaza la capa en el index de capas por una nueva. Invarianza: capa= n-1, limpia capas validas ya existentes"""
        self.capas[capa] = [[None for _ in range(self.w)] for _ in range(self.h)]

    def borrar_capa(self, capa):
        """Contrato: capa=index de la capa a borrar dentro de self.capas. Invarianza: capa=n-1, borra solo capas existentes"""
        self.capas.pop(capa)

    def escribir_pixel(self, p):
        """Contrato: p=Pixel, objeto con atributos x, y, capa y simbolo, escribe el simbolo en la lista de capas en la capa que especifica. Invarianza: solo acepta Pixels, trabaja solo con uno, todos sus atributos deben estar definidos y ser validos, x,y,capas = int, x,y,capas se escribiran siempre dentro del rango del canvas y siempre len(simbolo)=1"""
        if (p.x >= 0 and p.x <= self.lx) and (p.y >= 0 and p.y <= self.ly):
            if len(p.simbolo) == 1:
                self.capas[p.capa][p.y][p.x] = p

    def mostrar(self, m, index=0):
        """El output del render(Canvas), tiene dos modos c de componer, compondra la escena completa y m que mostrara la capa en el index dentro de la lista de capas. Contrato: m=modo, solo dos m y c, index=int. Invarianza: Base-0, index literal I-1, index debe existir, debe existir una capa base!=None, que este llena, en caso contrario espacios seran considerados no transparentes"""
        if m == "c":
            print("\n\n")
            buffer = ""
            for y in range(self.h):
                fila = ""
                for x in range(self.w):
                    char = " "
                    for capa in reversed(self.capas):
                        if capa[y][x] is None:
                            continue
                        if capa[y][x].transparente:
                            continue
                        char = capa[y][x].simbolo
                        break
                    fila += char
                buffer += fila + "\n"
            print(buffer)
        elif m == "m":
            buffer = ""
            for y in range(len(self.capas[index])):
                fila = ""
                for x in range(len(self.capas[index][y])):
                    char = " "
                    if self.capas[index][y][x] is None:
                        continue
                    if self.capas[index][y][x].transparente:
                        continue
                    char = self.capas[index][y][x].simbolo
                    fila += char
                buffer += fila + "\n"
            print(buffer)


class Pixel:
    """Simula el dato atomico que se puede introducir al canvas(simbolo), con atributos que el render(Canvas) usa para determinar como agregarlo y mostrarlo. Contrato: x,y,capa= int, simbolo=caracter. Invarianzas: x,y,capa deben ser int, si transparente es True, entonces " " sera tratado como parte del Pixel y no como vacio"""

    def __init__(self, x, y, capa, simbolo, transparente=False, color=None):
        self.x = x
        self.y = y
        self.capa = capa
        self.simbolo = simbolo
        self.transparente = transparente
        self.color = color


class Texto:
    def __init__(self, simbolo, m):
        self.simbolo = simbolo
        self.m = m

    def generar(self):
        if self.m == "h":
            for s in range(len(self.simbolo)):
                yield Pixel(s, 0, None, self.simbolo[s])
        if self.m == "v":
            for s in range(len(self.simbolo)):
                yield Pixel(0, s, None, self.simbolo[s])
        if self.m == "d":
            for s in range(len(self.simbolo)):
                yield Pixel(s, s, None, self.simbolo[s])

    def bbox(self):
        return (len(self.simbolo), 1)


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
                yield Pixel(self.x + i, self.y, None, self.simbolo)
        elif self.m == "v":
            for i in range(self.largo + 1):
                yield Pixel(self.x, self.y + i, None, self.simbolo)
        elif self.m == "d":
            for i in range(self.largo + 1):
                yield Pixel(self.x + i, self.y + i, None, self.simbolo)

    def bbox(self):
        if self.m == "h":
            return (self.largo + 1, 1)
        if self.m == "v":
            return (1, self.largo + 1)
        if self.m == "d":
            return (self.largo + 1, self.largo + 1)


class Rectangulo:
    def __init__(self, w, h, simbolo):
        self.w = w
        self.h = h
        self.simbolo = simbolo

    def generar(self):
        lados = [
            Linea(0, 0, self.h, self.simbolo, "v"),
            Linea(0, 0, self.w, self.simbolo, "h"),
            Linea(self.w, 0, self.h, self.simbolo, "v"),
            Linea(0, self.h, self.w, self.simbolo, "h"),
        ]
        for lado in lados:
            yield from lado.generar()


class Circulo:
    def __init__(self):
        pass


class Triangulo:
    def __init__(self):
        pass


class Sprite:
    def __init__(self, x, y, capa, shapes, fondo, behaviors):
        self.x = x
        self.y = y
        self.capa = capa
        self.shapes = shapes
        self.fondo = fondo
        self.w, self.h = self._calcular_bbox()
        self.dx = 1
        self.dy = 1
        self.behaviors = behaviors

    def generar_shapes(self):
        for shape in self.shapes:
            for i in shape.generar():
                if not self.fondo and i.simbolo == " ":
                    yield Pixel(self.x + i.x, self.y + i.y, self.capa, i.simbolo, True)
                elif self.fondo:
                    yield Pixel(self.x + i.x, self.y + i.y, self.capa, i.simbolo)

    def _calcular_bbox(self):
        max_w = 0
        max_h = 0
        for s in self.shapes:
            w, h = s.bbox()
            max_w = max(max_w, w)
            max_h = max(max_h, h)
        return max_w, max_h


class Bitmap:
    def __init__(self, data):
        self.data = data
        self.w = max(len(row) for row in self.data)
        self.h = len(self.data)

    def generar(self):
        for y in range(len(self.data)):
            for x in range(len(self.data[y])):
                yield Pixel(x, y, None, self.data[y][x])

    def bbox(self):
        w = max(len(f) for f in self.data)
        h = len(self.data)
        return (w, h)


class Scene:
    def __init__(self, canvas):
        self.canvas = canvas
        self.sprites = []
        self.input_state = set()

    def leer_input(self, input_state):
        while True:
            dr, _, _ = select.select([sys.stdin], [], [], 0)
            if not dr:
                break
            key = sys.stdin.read(1)
            self.input_state.add(key)

    def update(self):
        self.input_state.clear()
        self.leer_input(self.input_state)
        for i in self.sprites:
            for behavior in i.behaviors:
                behavior(i, self)

    def draw(self):
        for s in self.sprites:
            for p in s.generar_shapes():
                self.canvas.escribir_pixel(p)

    def render(self):
        self.canvas.mostrar("c")

    def clear(self, fondo):
        print("\033[H")
        for i in range(len(self.canvas.capas)):
            if i != fondo:
                self.canvas.limpiar(i)


def rebotar(sprite, scenes):
    sprite.x += sprite.dx
    sprite.y += sprite.dy
    if sprite.x <= 0 or sprite.x + sprite.w >= scenes.canvas.lx:
        sprite.dx *= -1
    if sprite.y <= 0 or sprite.y + sprite.h >= scenes.canvas.ly:
        sprite.dy *= -1


def input_move(sprite, scene):
    keys = scene.input_state
    if "a" in keys:
        sprite.x -= 1
    if "d" in keys:
        sprite.x += 1
    if "w" in keys:
        sprite.y -= 1
    if "s" in keys:
        sprite.y += 1


def colision(a, b):
    return a.x < b.x + b.w and a.x + a.w > b.x and a.y < b.y + b.h and a.y + a.h > b.y


def colision_rebote(sprite, scene):
    for other in scene.sprites:
        if other is sprite:
            continue
        if colision(sprite, other):
            if abs(sprite.x - other.x) > abs(sprite.y - other.y):
                sprite.dx *= -1
            else:
                sprite.dy *= -1


a = Canvas(98, 24, 2)

FPS = 30
frame_time = 1 / FPS
s = [
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

s = Sprite(0, 0, 1, [Bitmap(s)], True, [input_move])
o = Sprite(
    60,
    1,
    1,
    [Texto("arroz", "h")],
    True,
    [
        input_move,
    ],
)
fd = sys.stdin.fileno()
old_settings = termios.tcgetattr(fd)
tty.setcbreak(fd)
escena = Scene(a)
escena.sprites.append(s)
escena.sprites.append(o)
while True:
    escena.clear(0)
    escena.update()
    escena.draw()
    escena.render()
    time.sleep(0.1)
termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
