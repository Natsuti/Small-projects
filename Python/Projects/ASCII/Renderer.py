import sys


class Renderer:
    def __init__(self, canvas):
        self.canvas = canvas

    def convertir(self, p):
        if p is None or p.transparente:
            return " "
        estilo = p.estile or {}
        fg = estilo.get("fg")
        bg = estilo.get("bg")
        bold = estilo.get("bold", False)
        seq = ""
        if fg is not None:
            seq += f"\033[38;5;{fg}m"
        if bg is not None:
            seq += f"\033[48;5;{bg}m"
        if bold:
            seq += "\033[1m"
        return f"{seq}{p.simbolo}\033[0m"

    def render(self):
        buffer = ""
        for y in range(self.canvas.h):
            for x in range(self.canvas.w):
                p = None
                for capa in reversed(self.canvas.capas):
                    if capa[y][x] and not capa[y][x].transparente:
                        p = capa[y][x]
                        break
                buffer += self.convertir(p)
            buffer += "\n"
        sys.stdout.write(buffer)
