def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        #count the number of words in the file

        number_of_words = file_contents.split()
        print(len(number_of_words))

main()