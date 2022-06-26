from cs50 import get_string


def main():
    # get test from user
    text = get_string("Text: ")

    # count number of letters, words, sentence
    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    # calculate L & S
    L = (letters / words) * 100
    S = (sentences / words) * 100

    # calculate grade & print
    grade = round(0.0588 * L - 0.296 * S - 15.8)
    if (grade < 1):
        print("Before Grade 1")
    elif (grade > 16):
        print("Grade 16+")
    else:
        print(f"Grade {grade}")


# calculate letters
def count_letters(text):
    count = 0
    for char in text:
        if (char.isalpha()):
            count += 1
    return int(count)


# calculate words
def count_words(text):
    count = 0
    if (len(text) > 0):
        count = 1
        for char in text:
            if (char == " "):
                count += 1
    return int(count)


# calculate sentence
def count_sentences(text):
    count = 0
    for char in text:
        if (char == "." or char == "!" or char == "?"):
            count += 1
    return int(count)


main()