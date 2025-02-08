#3a Diskutera följande kod. Räcker det med ett testfall för att testa funktionen?
# Returnerar ett heltal med antalet vokaler som finns i ordet (aeiouyåäö)

#def count_vowels(word):
#    return None

#3b Skriv färdigt funktionen count_vowels med hjälp av TDD-metoden, red → green → refactor:
def count_vowels(my_word):
    vokaler = ["a", "e", "i", "o", "u", "y", "å", "ä", "ö"]
    count = 0
    for i in range(len(my_word)):
        if vokaler.count(my_word[i].lower()) == 1:
            count += 1
    print(f"Number of vowels in the word '{my_word}' is {count}")
    return count

count_vowels("aeiouyåäö")
