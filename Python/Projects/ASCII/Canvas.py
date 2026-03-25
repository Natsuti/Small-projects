class Canvas:
    """Simula una pantalla wxh, cada capa/matriz es un lienzo, cuando toca mostrar combina todos los lienzos/capas para crear una escena. Contrato: w=witdh, h=height, w,h y capas deben ser int, capas=numero de lienzos, el limite del canvas es w-1, h-1, todos los methods de canvas trabajan con Pixels y solo Pixels. Invarianza= w,h siempre int positivos, siempre debe haber aunque sea una capa(base), coordenadas siempre deben ser accedidas [y][x]/(y,x), se recorre por filas(y) no por x(lineas)"""

    def __init__(self, w=134, h=30, capas=1):
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

    def escribir_pixels(self, lp):
        """Contrato: p=Pixel, objeto con atributos x, y, capa y simbolo, escribe el simbolo en la lista de capas en la capa que especifica. Invarianza: solo acepta Pixels, trabaja solo con uno, todos sus atributos deben estar definidos y ser validos, x,y,capas = int, x,y,capas se escribiran siempre dentro del rango del canvas y siempre len(simbolo)=1"""
        for p in lp:
            if (p.x >= 0 and p.x <= self.lx) and (p.y >= 0 and p.y <= self.ly):
                if len(p.simbolo) == 1:
                    self.capas[p.capa][p.y][p.x] = p

    def get_pixel(self, x, y):
        return self.capas[0][y][x]
