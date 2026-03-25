from ASCII import (
    Canvas,
    Sprite,
    Scene,
    Rectangulo,
    Texto,
    Linea,
    Bitmap,
)

e = Scene(Canvas())
e.add_sprite(
    Sprite(
        40,
        0,
        0,
        [Rectangulo(0, 3, 10, 5, "|", "-")],
        {"fg": 4, "bg": 4, "bold": True},
    )
)
e.start()
