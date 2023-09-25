# function to get number of words in a string
def get_num_words(text):
    return len(text.split())

def get_letter_map(text):
    letters = {}
    for l in text.lower():
        if l.isalpha() == True:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
    return letters

def main(): 
    with open("./books/frakenstein.txt") as f:
        text = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{get_num_words(text)} words found in the document\n")
        letter_map = get_letter_map(text)
        sorted_letter_list = sorted(list(letter_map))
        for letter in sorted_letter_list:
            print(f"The '{letter}' character was found {letter_map[letter]} times")
        print("--- End report ---")

main()

