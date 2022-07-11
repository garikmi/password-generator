import random
import string
import re

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


def generate_password(separators_enabled=True, fake_words_enabled=False, uppercase_enabled=True, numbers_enabled=True):
    password = ""
    
    parts = 3
    separators = ['-', '_', '.']
    characters = string.ascii_letters + '0123456789'
    for count in range(parts):
        if not uppercase_enabled and not numbers_enabled:
            characters = string.ascii_lowercase
        if uppercase_enabled and not numbers_enabled:
            characters = string.ascii_letters
        if not uppercase_enabled and numbers_enabled:
            characters = string.ascii_lowercase + '0123456789'
            
        if fake_words_enabled:
            part_length = 2
        else:
            part_length = random.randrange(4, 8)
        
        uppercase_part = random.randrange(2)
        for _ in range(part_length):
            if fake_words_enabled:
                list = generateSyllables()
                if uppercase_enabled and count == uppercase_part:
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
while selectedChoice not in ['a', 'b', 'c']:
    selectedChoice = input('Which password style would you like to generate?\na. y8b9m9_GjCl.jf4mY\nb. QDasFGoB9d2uuBq6\nc. linload-zoomplan_tytes4\n-> ')
    
    
# TODO: Choose password length
# TODO: Choose parts length
# TODO: Choose custom separator(s)
# TODO: Should include uppercase letters or words : DONE
# TODO: Should include numbers                    : DONE
# TODO: Should include symbols
    

def main():
    uppercase = ''
    while uppercase != 'y' and uppercase != 'n':
        uppercase = input('Would you like to include uppercase words (y/n)? -> ')
    numbers = ''
    while numbers != 'y' and numbers != 'n':
        numbers = input('Would you like to include numbers (y/n)? -> ')
    if uppercase == 'y':
        uppercase = True
    if uppercase == 'n':
        uppercase = False
    if numbers == 'y':
        numbers = True
    if numbers == 'n':
        numbers = False
    
    if selectedChoice == 'a':
        print(generate_password(True, False, uppercase, numbers))
    
    if selectedChoice == 'b':
        print(generate_password(False, False, uppercase, numbers))
    
    if selectedChoice == 'c':
        print(generate_password(True, True, uppercase, numbers))
    
if __name__ == "__main__":
    main()
    