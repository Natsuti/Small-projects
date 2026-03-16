import logging

logging.basicConfig(level=logging.DEBUG, format="%(message)s")
bitmap = [
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
message = input("@ ")
for i in range(len(bitmap)):
    for j in range(len(bitmap[i])):
        if bitmap[i][j] == " ":
            print(" ", end="")
        else:
            print(message[j % len(message)], end="")
    print()
