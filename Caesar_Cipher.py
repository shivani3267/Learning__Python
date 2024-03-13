#Caesar Cipher - a simple technique of encryption and decryption

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m',
        'n','o','p','q','r','s','t','u','v','w','x','y','z']

#encryption function
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        position=alphabet.index(char)
        new_position=(position+shift_key)%26
        cipher_text+=alphabet[new_position]
    print("Here's is the text after encryption: ",cipher_text)

#decryption function
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        position=alphabet.index(char)
        new_position=(position-shift_key)%26
        plain_text+=alphabet[new_position]
    print("Here's is the text after decryption: ",cipher_text)

#main code
wanna_end=False
while not wanna_end:
    what_to_do=input("Type 'encrypt for encryption, type 'decrypt for decryption:\n").lower()
    
    if what_to_do=="encrypt":
        text=input("Type your message:\n").lower()
        shift=int(input("Enter shift key:\n"))
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        text=input("Type your message:\n")
        shift=int(input("Enter shift key:\n"))
        decryption(cipher_text=text,shift_key=shift)
    else:
        print("Wrong input")
    play_again=input("Type yes to continue and type no to exit:\n").lower()
    if play_again=="no":
        print("Have a nice day! Bye...")
        wanna_end=True