import math
import random
import string
import re
import linecache

def random_word():
    with open('words.txt', 'r') as file:
        word = linecache.getline('words.txt', random.randrange(sum(1 for line in file)))
        file.close()
    return word

def generateSyllables():
    test = [syllable.strip('\n') for syllable in re.findall("[^aeiouy]*[aeiouy]+(?:[^aeiouy]*$|[^aeiouy](?=[^aeiouy]))?", random_word())]
    return test

def generateFakeWord():
    return random.choice(generateSyllables()) + random.choice(generateSyllables())
 
def generate_password(length, parts, separators, symbols, should_words, should_uppercase, should_numbers):
    password = ""
    
    if length == 0:
        length = random.randrange(5, 32)
    if parts is None:
        parts = 3
    if separators is None:
        separators = '-._'
    if symbols is None:
        symbols = '!@#$%&*()_-+=[]:;?'
        
    everyStep = round(length / (1 if parts == 0 else parts))
    countSeparators = 0

    list = []

    if should_uppercase:
        list.append(string.ascii_letters)
    else:
        list.append(string.ascii_lowercase)
    
    if should_numbers:
        list.append("0123456789")
    
    if len(symbols) > 0:
        list.append(symbols)
        
    for index in range(0, length):
        password += random.choice(list[random.randrange(0, len(list))])
        if len(separators) > 0 and ((index+1) % everyStep) == 0 and index+1 != length and countSeparators < parts-1:
            countSeparators += 1
            password += random.choice(separators)
    
    return password


#selectedChoice = ""
#while selectedChoice not in ['a', 'b', 'c']:
#   selectedChoice = input('Which password style would you like to generate?\na. y8b9m9_GjCl.jf4mY\nb. QDasFGoB9d2uuBq6\nc. linload-zoomplan_tytes4\n-> ')
    
    
# TODO: Choose password length                    : DONE
# TODO: Choose parts length                       : DONE
# TODO: Choose custom separator(s)                : DONE
# TODO: Should include uppercase letters or words : DONE
# TODO: Should include numbers                    : DONE
# TODO: Should include symbols                    : DONE
# TODO: Should include fake words                 :
    

def main():
    print("\nTesting:\nlen: 10, parts: 2, not uppercase, not numbers -> " + generate_password(10, 2, '', '', True, False, False))
    print("len: 10, parts: 3, not uppercase, not numbers -> " + generate_password(10, 3, None, '', True, False, False))
    print("len: 10, parts: 4, not uppercase, not numbers -> " + generate_password(10, 4, None, '', True, False, False))
    print("len: 10, parts: 9, not uppercase, not numbers -> " + generate_password(10, 9, None, '', True, False, False))
    print("len: 10, parts: 10, not uppercase, not numbers -> " + generate_password(10, 10, None, '', True, False, False))
    print("len: 10, parts: 0, not uppercase, not numbers -> " + generate_password(10, 0, None, '', True, False, False))
    
#   uppercase = ''
#   while uppercase != 'y' and uppercase != 'n':
#       uppercase = input('Would you like to include uppercase words (y/n)? -> ')
#   numbers = ''
#   while numbers != 'y' and numbers != 'n':
#       numbers = input('Would you like to include numbers (y/n)? -> ')
#   if uppercase == 'y':
#       uppercase = True
#   if uppercase == 'n':
#       uppercase = False
#   if numbers == 'y':
#       numbers = True
#   if numbers == 'n':
#       numbers = False
#   
#   if selectedChoice == 'a':
#       print(generate_password(True, False, uppercase, numbers))
#   
#   if selectedChoice == 'b':
#       print(generate_password(False, False, uppercase, numbers))
#   
#   if selectedChoice == 'c':
#       print(generate_password(True, True, uppercase, numbers))
        
if __name__ == "__main__":
    main()
    