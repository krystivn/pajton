
import sys
tries = 5
word = "wisielec"
letter_input = []
used_letters = []

for l in word: letter_input.append("_")

def find_index(word,letter): #przypisanie indeksu do wybranej litery
    indexes = []
    
    for index, letter_in_word in enumerate(word): #enumerate przypisuje indeks
        if letter == letter_in_word:
            indexes.append(index)

    return indexes

while True:

    letter=input("Wybierz litere: ")
    find_index(word, letter)
    used_letters.append(letter)
    print("Uzyte litery: ",used_letters)
   

    found_index = find_index(word, letter) 

    if len(found_index) == 0: #usuwanie prob
        tries -= 1
        print("W slowie nie ma takiej litery. Pozostala liczba prob: " + str(tries))
        if tries == 0:
            print("KONIEC GRY")
            sys.exit(0)
    else:
        for index in found_index:
            letter_input[index] = letter
            print(letter_input)

    if "_" not in letter_input:
        print("Gratulacje, wygrales!")
        sys.exit(0)   
    



    
