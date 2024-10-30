def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        print_report(book_path, count_words(file_contents), count_characters(file_contents))
    

def count_words(text_file):
    #split the string and assign the number of words to a variable, and then return it
    number_of_words = text_file.split()
    return len(number_of_words)

def count_characters(text_file):
    #dictionary
    letter_count = {}
    #convert to lower case
    lowered_text = text_file.lower()
    #loop through each character in the text file
    
    for character in lowered_text:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1 
    return letter_count

def print_report(path, total_words, character_counts):
    
    print(f"--- Begin report of {path} ---")
    #get the total count of all words
    print(f"There were {total_words} words found in the document.")
    #print how many times each character was found
    for k, v in sorted(character_counts.items()):
        if k.isalpha() == True:
            print(f"The character '{k}' was found {v} times")
    

main()