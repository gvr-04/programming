import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
d = {rows.letter: rows.code for (index, rows) in df.iterrows()}


def generate_phonetic():
    try:
        word = input("Enter a word: ")
        output = [d[i.upper()] for i in word]
    except KeyError:
        print("sorry only letter in the alphabets please...")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()
