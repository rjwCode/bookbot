from stats import num_of_words, get_num_chars, sort_counts, output_sorted_list

def get_book_text(file_path):
    with open(file_path) as file:
        contents_as_str = file.read()
    return contents_as_str


def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    
        text = get_book_text(book_path)
        word_count = num_of_words(text)
        char_counts = get_num_chars(text)
        sorted_list = sort_counts(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        output_sorted_list(sorted_list)
        print("============= END ===============")


main()
