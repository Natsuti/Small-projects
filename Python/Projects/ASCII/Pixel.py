class Pixel:
    """Simula el dato atomico que se puede introducir al canvas(simbolo), con atributos que el render(Canvas) usa para determinar como agregarlo y mostrarlo. Contrato: x,y,capa= int, simbolo=caracter. Invarianzas: x,y,capa deben ser int, si transparente es True, entonces " " sera tratado como parte del Pixel y no como vacio"""

    def __init__(self, x, y, capa, z, simbolo, estile=None, transparente=False):
        self.x = x
        self.y = y
        self.capa = capa
        self.z = z
        self.simbolo = simbolo
        self.transparente = transparente
        self.estile = estile or {}
