def caesar(text,shift,encrypt=True):
    if not isinstance(shift,int):
        return ("Shift must be an integer.")
    if shift<1 or shift>25:
        return ("Shift must be between 1 and 25.")
    alphabet="abcdefghijklmnopqrstuvwxyz"
    if  encrypt:
        shift=-shift
        shifted_alphabet=alphabet[shift:]+alphabet[:shift]
        translation_table=str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
        return text.translate(translation_table)
def encrypt(text,shift):
        return caesar(text,shift,encrypt=False)
def decrypt(text,shift):
        return caesar(text,shift,)
encrypted_text=("Xbaxn vf gur TBNG")
decrypted_text=decrypt(encrypted_text,13)
print(decrypted_text)