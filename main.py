from stats import get_num_of_words, count_characters

import sys

def get_book_text(file_to_path):
    with open(file_to_path) as f:
        output = f.read()
        return output

def sort_on(items):
    return items["num"]

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    txt = get_book_text(filepath)
    num_of_words = get_num_of_words(txt)

    count_char_list = count_characters(txt)
    count_char_list.sort(reverse=True, key=sort_on)

    #print(txt)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for i in range(0, len(count_char_list)):
        tmp = count_char_list[i]
        print(f"{tmp["char"]}: {tmp["num"]}")
    print("============= END ===============")

main()



