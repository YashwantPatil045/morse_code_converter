morse_data = {
    '/': '/',
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '-.', 'h': '....', 'i': '..',
    'j': '.-', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',

    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', '0': '-----'
}
chars = "~!@#$%^&*()_+="


def morse_code_converter():
    msg = input("Write your message: ")
    words = msg.split()
    sep_msg = ""
    for word in words:
        sep_words = [word + "/"]
        for letters in sep_words:
            for letter in list(letters):
                if letter not in chars:
                    sep_msg += morse_data[letter.lower()] + " "
                else:
                    print("Special characters won't be converted into Morse Code. Try again")
                    return

    print(f"Here is a Morse Code: {sep_msg[:-2]}")
    if len(words) > 1:
        print("(Note: Words are separated by '/')")


morse_code_converter()



