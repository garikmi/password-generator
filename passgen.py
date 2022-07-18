from os import sep
import random
import string
import re
import linecache


def random_word():
    with open('words.txt', 'r') as file:
        word = linecache.getline('words.txt', random.randrange(sum(1 for line in file))).strip('\n')
        file.close()
    return word


def generate_syllables():
    syllables = []
    while not syllables:
        syllables = [syllable.strip('\n') for syllable in re.findall("[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=["
                                                                     "^aeiouy]))?", random_word())]
    return syllables


def generate_fake_word():
    return random.choice(generate_syllables()) + random.choice(generate_syllables())


# Enter None for default separators or symbols.
# Enter '' to skip separators or symbols.
def generate_password(length, parts, separators, symbols, should_words, should_uppercase, should_numbers):
    password = ''

    if length == 0:
        length = random.randrange(5, 32)
    if parts is None:
        parts = 3
    if separators is None:
        separators = '-._'
    if symbols is None:
        symbols = '!@#$%&*()_-+=[]:;?'

    every_step = round(length / (1 if parts == 0 else parts))
    count_separators = 0

    collection = []

    if should_uppercase:
        collection.append(string.ascii_letters)
    else:
        collection.append(string.ascii_lowercase)

    if should_numbers:
        collection.append('0123456789')

    if len(symbols) > 0:
        collection.append(symbols)

    for index in range(0, length):
        password += random.choice(collection[random.randrange(0, len(collection))])
        if len(separators) > 0 and ((index+1) % every_step) == 0 and index+1 != length and count_separators < parts-1:
            count_separators += 1
            password += random.choice(separators)

    return password


def generate_word_password(parts, separators, should_uppercase, should_numbers):
    password = ''

    if parts == 0:
        parts = random.randrange(2, 6)
    if separators is None:
        separators = '-._'

    for index in range(parts):
        if should_numbers and bool(random.getrandbits(1)):
            password += generate_fake_word().upper()
        else:
            password += generate_fake_word()
        if should_numbers:
            password += random.choice('0123456789')
        if index+1 < parts and len(separators) > 0:
            password += random.choice(separators)

    return password


def main():
    pass


if __name__ == "__main__":
    main()
