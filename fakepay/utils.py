from random import choice


def random_alphanumeric(length: int) -> str:
    """Gera uma string aleatória com o comprimento indicado"""
    chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D",
             "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
             "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f",
             "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
             "u", "v", "w", "x", "y", "z"]
    rand_str = ""
    for i in range(length):
        rand_str += choice(chars)

    return rand_str
