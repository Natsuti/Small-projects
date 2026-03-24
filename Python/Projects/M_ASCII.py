from ASCII import Canvas, Sprite, Scene, Rectangulo, Linea

e = Scene(Canvas())
e.add_sprite(
    Sprite(
        40,
        0,
        0,
        [
            Rectangulo(20, 10, "|", "-"),
            Linea(10, 11, 10, "*", "v"),
            Linea(10, 11, 5, "*", "di"),
            Linea(10, 11, 5, "*", "d"),
        ],
        30,
    )
)
e.canvas.establecer_color(16)
e.draw()
e.render()
