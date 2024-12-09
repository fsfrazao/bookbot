
def get_character_freq(string):
    character_freq = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0,
                      "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
                      "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0,
                      "v":0, "w":0, "y":0, "x":0, "z":0 }

    string_lwr = string.lower()
    for c in string_lwr:
        if c in character_freq:
            character_freq[c] += 1

    return character_freq   


def count_words(string):
    return len(string.split())


def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()

    print(count_words(file_contents))
    print(get_character_freq(file_contents))

main()