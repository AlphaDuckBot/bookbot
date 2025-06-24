from stats import get_num_of_words, count_characters

def get_book_text(filepath):
    with open(filepath) as f:
        output = f.read()
        return output

def main():
    txt = get_book_text("books/frankenstein.txt")
    num_of_words = get_num_of_words(txt)
    print(f"{num_of_words} words found in the document")
    count_char_dict = count_characters(txt)
    print(count_char_dict)
    #print(txt)

main( )


