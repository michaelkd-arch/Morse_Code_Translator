import string

alphanumeric = list(string.ascii_lowercase) + [str(i) for i in range(9, -1, -1)]

morse_code_characters = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.',
                         '....', '..', '.---', '-.-', '.-..', '--', '-.',
                         '---', '.--.', '--.-', '.-.', '...', '-', '..-',
                         '...-', '.--', '-..-', '-.--', '--..', '----.',
                         '---..', '--...', '-....', '.....', '....-',
                         '...--', '..---', '.----', '-----']

morse_code_trans = {alphanumeric[i]: morse_code_characters[i] for i in range(0, len(alphanumeric))}

translation = ''

print('Note that only alphanumerical characters and non empty inputs are allowed')

while len(translation) == 0:
    user_input = str(input('Please enter your input here: ')).lower()
    if user_input.isalnum() and len(user_input) > 0:
        for a in user_input:
            translation += morse_code_trans[a]
            translation += ' '
        print(translation)
    else:
        print('You entered a non alphanumeric character or no characters at all.\nTry again.')
        continue




