import itertools
import string



def char_occurence(ciphertext):
    chars = string.ascii_uppercase + string.digits
    occurences = {}
    for char in chars:
        occurences[char] = ciphertext.count(char)
    return occurences

def espace_possible(ciphertext):
    chars = string.ascii_uppercase + string.digits
    combinations = itertools.permutations(chars,3)
    combination_strings = [''.join(comb) for comb in combinations]
    for i in range(len(ciphertext)-3):
        test = ciphertext[i:i+3]
        if test in combination_strings:
            combination_strings.remove(test)
    return combination_strings



if __name__ == "__main__":
    with open("ciphertext.txt","r") as f:
        ciphertext = f.read()
        ciphertext = ciphertext.replace(" ","").replace("\n","")
        print(char_occurence(ciphertext))


