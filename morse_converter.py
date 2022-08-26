morse_data = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '-.', 'h': '....', 'i': '..',
    'j': '.-', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',

    '.': ".-.-.-", ',': "--..--", '?': "..--..", "'": ".----.", '!': "-.-.--", '(': "-.--.", ')': "-.--.-",
    '&': ".-...", ':': "---...", ';': "-.-.-.", '=': "-...-", '+': ".-.-.", '-': "-....-", '_': "..__._", '"': ".-..-.",
    '$': "...-..-", '@': ".--.-.",

    '/': '/'
}


def morse_code_converter():
    msg = input("Write your message: ")
    words = list(msg.replace(" ", '/'))
    code = []
    for letter in words:
        try:
            code.append(morse_data[letter.lower()])
        except KeyError:
            return print("Sorry... Some characters can't be converted into Morse Code.")
    final_msg = " ".join(code)
    print(f"Here's your message converted into the Morse code:\n\n {final_msg}")
    if "/" in final_msg:
        print("\n(Note: Words are separated by '/')")


morse_code_converter()
