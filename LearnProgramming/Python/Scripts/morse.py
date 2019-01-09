morse_words = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
               'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
               'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
               'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
               'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..'}

morse_numbers = {'1': '.----', '2': '..---', '3': '...--', '4': '....-',
                 '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                 '9': '----.', '0': '-----'}


def word_to_morse(word):
    """convert words and numbers to morse code"""
    for i in range(len(word)):
        if word[i] in morse_words.keys():
            print(morse_words[word[i]]),
        elif word[i] in morse_numbers.keys():
            print(morse_numbers[word[i]]),
        elif word[i] == ' ':
            print'/',
        else:
            print(word[i]),


new_enter = raw_input("Please enter your words:")
while new_enter != ' ':
    word_to_morse(new_enter.upper())
    new_enter = raw_input("\nPlease enter your words or blank space to quit:")
