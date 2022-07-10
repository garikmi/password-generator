import random
import string
import re


parts = 3
separators = ['-', '_', '.']
characters = string.ascii_letters + '0123456789'


def random_word(file):
    file.seek(0)
    word = next(file)
    for num, line in enumerate(file, 2):
        if random.randrange(num):
            continue
        word = line
    return word

def generateSyllables():
    syllables = []
    with open('words.txt', 'r') as file:
        while not syllables:
            syllables = [syllable.strip('\n') for syllable in re.findall("[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?", random_word(file))]
    file.close()
    return syllables


def generate_password(separators_enabled=True, fake_words_enabled=False, numbers_enabled=True):
    password = ""
    for count in range(parts):
        if fake_words_enabled:
            part_length = 2
        else:
            part_length = random.randrange(4, 8)
        
        uppercase_part = random.randrange(2)
        for _ in range(part_length):
            if fake_words_enabled:
                list = generateSyllables()
                if count == uppercase_part:
                    password += random.choice(list).upper()
                else:
                    password += random.choice(list)
            else:
                password += random.choice(characters)
        
        if numbers_enabled:
            should_put_number = bool(random.getrandbits(1))
            if should_put_number:
                password += str(random.randrange(0, 9))
            
        if separators_enabled:
            if count < parts-1:
                password += random.choice(separators)
    return password
 

selectedChoice = ""
while selectedChoice not in ['a', 'b', 'c', '1', '2', '3']:
    selectedChoice = input('Which password style would you like to generate?\na. y8b9m9_GjCl.jf4mY\nb. QDasFGoB9d2uuBq6\nc. linload-zoomplan_tytes4\n-> ')
    
    
if selectedChoice == 'a':
    print(generate_password())
    
if selectedChoice == 'b':
    length = ''
    while not length.isnumeric() and length != 'n':
        length = input('Enter length of the password or \'n\' to choose random -> ')
    if length.isnumeric():
        print(generate_password(False, False, True))
    else:
        print(generate_password(False, False, True))
    
if selectedChoice == 'c':
    print(generate_password(True, True, True))
    