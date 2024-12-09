
def get_letter_freq(string):
    letter_freq = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0,
                      "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
                      "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0,
                      "v":0, "w":0, "y":0, "x":0, "z":0 }

    string_lwr = string.lower()
    for c in string_lwr:
        if c in letter_freq:
            letter_freq[c] += 1

    return letter_freq   

def sort_letters(dict):
    letter_list = [{"letter":letter, "freq":dict[letter]} for letter in dict ]

    letter_list.sort(reverse=True, key=lambda d:d["freq"])
    return letter_list



def count_words(string):
    return len(string.split())


def generate_report(book):
    with open(book) as f:
        book_contents = f.read()

    num_words = count_words(book_contents)
    letter_freq = get_letter_freq(book_contents)
    sorted_letter_freq = sort_letters(letter_freq)



    print(f"--- Begin report of {book} ---")
    print(f"\n{num_words} words found in the document\n")

    for l in sorted_letter_freq:
        print(f"The {l['letter']} character was found {l['freq']} times" )
    print(f"\n--- End report ---")


generate_report("books/frankenstein.txt")