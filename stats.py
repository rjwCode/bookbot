def num_of_words(book_text):
    word_list = book_text.split()
    return len(word_list)

def get_num_chars(book_text):
    chars_counts = {}
    lower_case = book_text.lower()
    for char in lower_case:
        if char not in chars_counts.keys():
            chars_counts[char] = 1
        else:
            chars_counts[char] += 1

    return chars_counts

def sort_counts(count_dict):
    dict_as_list = list(count_dict.items())
    dict_as_list.sort(key=lambda entry: entry[1], reverse=True)
    return dict_as_list

def output_sorted_list(sorted):
    for dictionary in sorted:
        if dictionary[0].isalpha() == True:
            print(f"{dictionary[0]}: {dictionary[1]}\n")
