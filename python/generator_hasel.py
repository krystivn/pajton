import sys
import random
import string

password = []
no_of_chars = int(input("podaj liczbe znakow w hasle:"))
chars_left = no_of_chars


def update_chars_left(chars):
    global chars_left
    checking = True
    while checking:
        if chars < 0 or chars > chars_left:
            print("podano liczbe znakow spoza przedzialu 0,", chars_left,)
            chars = int(input("sprobuj jeszcze raz:"))
        else:
            chars_left -= chars
            checking = False

    if no_of_chars < 8:
        print("haslo musi miec co najmniej 8 znakow.")

lowercase_letters = int(input("podaj liczbe malych liter w hasle: "))
update_chars_left(lowercase_letters)
uppercase_letters = int(input("podaj liczbe duzych liter w hasle: "))
update_chars_left(uppercase_letters)
numbers = int(input("podaj liczbe cyfr w hasle: "))
update_chars_left(numbers)
special_characters = int(input("podaj liczbe znakow specjalnych w hasle: "))
update_chars_left(special_characters)

if chars_left > 0:
    lowercase_letters += chars_left
    print("podano za malo znakow, pozostale zostana uzupelnione malymi literami")

for _ in range(no_of_chars):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if numbers > 0:
        password.append(random.choice(string.digits))
        numbers -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1    

random.shuffle(password)
print("wygenerowane haslo to: ", "".join(password))
            
      


