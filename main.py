def get_book_text(filepath):
    with open(filepath) as f:
        output = f.read()
        return output

def main():
    txt = get_book_text("books/frankenstein.txt")
    print(txt)

main( )


