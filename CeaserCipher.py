alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift, cipher_direction):
    end_text=""
    if cipher_direction == 'decode':
        shift *= -1
    for letter in start_text:
        if letter not in alphabets:
            end_text += letter
        else:
            shifted_index = (alphabets.index(letter) + shift) % len(alphabets)
            end_text += alphabets[shifted_index]
    print(f"The {cipher_direction}d text is : {end_text}")

def restart():
    direction = input("\nType 'Encode' to encrypt or 'Decode' to decrypt : \n")
    text = input("\nType your Message : \n").lower()
    shift = int(input("\nType the shift number or Key :"))
    shift = shift % 25
    caesar(start_text=text, shift=shift, cipher_direction=direction)
choice = 'yes'

while choice == 'yes':
    restart()
    choice = input("\nWould you Like to Cipher Again? (yes/no) :")
