
import sys
tries = 5
word = "wisielec"
list = []
used_letters = []

for l in word: list.append("_")

def find_index(word,letter): #przypisanie indeksu do wybranej litery
    indexes = []
    
    for index, letter_in in enumerate(word): #enumerate przypisuje indeks
        if letter == letter_in:
            indexes.append(index)

    return indexes

while True:

    letter=input("wybierz litere: ")
    find_index(word, letter)
    used_letters.append(letter)
    print("uzyte litery: ",used_letters)
   

    found_index = find_index(word, letter) 

    if len(found_index) == 0: #usuwanie prob
        tries -= 1
        print("W slowie nie ma takiej litery. Pozostala liczba prob: " + str(tries))
        if tries == 0:
            print("KONIEC GRY")
            sys.exit(0)
    else:
        for index in found_index:
            list[index] = letter
            print(list)

    if "_" not in list:
        print("gratulacje, wygrales")
        sys.exit(0)   
    



    
