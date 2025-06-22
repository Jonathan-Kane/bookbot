from stats import count_words, get_book_text, get_character_dict, dict_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def main():
    file_path = sys.argv[1]
    text = get_book_text(file_path)
    num_words = count_words(text)
    character_dict = get_character_dict(text)
    dictionary_list = dict_list(character_dict)
    # print(f"{num_words} words found in the document") 
    # print(get_character_number(text))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dictionary in dictionary_list:
        print(f"{dictionary['name']}: {dictionary['num']}")
    print("============= END ===============")
main()