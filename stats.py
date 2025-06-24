def get_num_of_words(text_string):
    list = text_string.split()
    amount = len(list)
    return amount

def count_characters(text_string):
    output_dictionary = dict()
    the_list = []
    lowercase_string = text_string.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for i in range(0, len(alphabet)):
        counter = 0
        for char in lowercase_string:
            if char in alphabet[i]:
                counter += 1

        output_dictionary["char"] = f"{alphabet[i]}"
        output_dictionary["num"] = counter
        the_list.append(output_dictionary)
        output_dictionary = dict()
        
    return the_list
