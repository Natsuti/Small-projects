class Canvas:
    """Simula una pantalla wxh, cada capa/matriz es un lienzo, cuando toca mostrar combina todos los lienzos/capas para crear una escena. Contrato: w=witdh, h=height, w,h y capas deben ser int, capas=numero de lienzos, el limite del canvas es w-1, h-1, todos los methods de canvas trabajan con Pixels y solo Pixels. Invarianza= w,h siempre int positivos, siempre debe haber aunque sea una capa(base), coordenadas siempre deben ser accedidas [y][x]/(y,x), se recorre por filas(y) no por x(lineas)"""

    def __init__(self, w=134, h=30, bg=12, capas=1):
        self.w = w
        self.h = h
        self.bg = bg
        self.capas = [
            [[None for _ in range(self.w)] for _ in range(self.h)] for _ in range(capas)
        ]
        self.lx = w - 1
        self.ly = h - 1

    def establecer_color(self, color):
        self.bg = color

    def crear_capa(self):
        """Contrato: self.w=width y self.h=height, 1 capa por uso. Invarianza:"""
        self.capas.append([[None for _ in range(self.w)] for _ in range(self.h)])

    def limpiar(self, capa):
        """Contrato: capa=index dentro de la lista de capas self.capas, reemplaza la capa en el index de capas por una nueva. Invarianza: capa= n-1, limpia capas validas ya existentes"""
        self.capas[capa] = [[None for _ in range(self.w)] for _ in range(self.h)]

    def borrar_capa(self, capa):
        """Contrato: capa=index de la capa a borrar dentro de self.capas. Invarianza: capa=n-1, borra solo capas existentes"""
        self.capas.pop(capa)

    def escribir_pixels(self, lp):
        """Contrato: p=Pixel, objeto con atributos x, y, capa y simbolo, escribe el simbolo en la lista de capas en la capa que especifica. Invarianza: solo acepta Pixels, trabaja solo con uno, todos sus atributos deben estar definidos y ser validos, x,y,capas = int, x,y,capas se escribiran siempre dentro del rango del canvas y siempre len(simbolo)=1"""
        for p in lp:
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
                    fila += f"\033[{38};{5};{0};{48};{5};{self.bg}m{char}"
                buffer += fila + "\033[0m" + "\n"
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
