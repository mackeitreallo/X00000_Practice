#Default Database
from replit import clear
import Final_Application_Database
restart = True

#Looper
while restart == True:
    clear()
    condition = ""
    control = ""
    to_be_encoded = []
    check_control = False
    check_text = False
    check_factor = False

#INPUT VERIFICATION
    while check_control != True:
        control = (input("\nWhat do you want to do? 'Encode' or 'Decode'?: ")).lower()
        clear()
        if control == "encode" or control == "decode":
            check_control = True
        else:
            print("\nINVALID INPUT!")

#ENCODE AND DECODE AI MODIFIER
    if control == "encode":
        condition = "message"
    else:
        condition = "code"

#TEXT INPUT VERIFICATION
    while check_text != True:
        text = (input(f"Enter the {condition} below to {control}\n"))
        response_text = input("Are you sure? Y/N: ")
        clear()
        if response_text == "Y":
            check_text = True

#STRING FACTOR INPUT VERIFICATION
    while check_factor != True:
        factor = int(input("\nHow many string factors you want to use?: "))
        response_factor = input("Are you sure? Y/N: ")
        clear()
        if response_factor == "Y":
            check_factor = True

#Word Encoder and Decoder
    def encode(t = text, fad = Final_Application_Database, f = factor):
        translate_encode = []
        translated_encode = []
        output = ""
        for n in range(len(t)):
            translate_encode += t[n]
            if translate_encode[n] in fad.letters:
                x = (fad.letters).index(translate_encode[n])
                translated_encode += fad.letters[x + f]
                output += translated_encode[n]
            elif translate_encode[n] in fad.numbers:
                x = (fad.numbers).index(translate_encode[n])
                translated_encode += fad.numbers[x + f]
                output += translated_encode[n]
            else:
                translated_encode += t[n]
                output += translated_encode[n]
        print(f"\nYour encrypted message is: {output}")
            
    def decode(t = text, fad = Final_Application_Database, f = factor):
        translate_decode = []
        translated_decode = []
        output = ""
        for n in range(len(t)):
            translate_decode += t[n]
            if translate_decode[n] in fad.letters:
                x = (fad.letters).index(translate_decode[n])
                translated_decode += fad.letters[x - f]
                output += translated_decode[n]
            elif translate_decode in fad.numbers:
                x = (fad.numbers).index(translate_decode[n])
                translated_decode += fad.numbers[x - f]
                output += translated_decode[n]
            else:
                translated_decode += t[n]
                output += translated_decode[n]
        print(f"\nYour decrypted message is: {output}")
            
    if control == "encode":
        encode()
    else:
        decode()
        
    again = input("\nDo you want to restart again? Y/N: ")
    if again == "N":
        restart = False
        clear()
        print("\nGoodbye!")