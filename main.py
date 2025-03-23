from stats import *
from sys import argv, exit

    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    text = get_book_text(path_to_file)
    print("----------- Word Count ----------")
    print(f"Found {len(text.split())} total words")
    print("-------- Character Count --------")
    char_counts = char_count(text)
    sorted_chars = sort_chars_by_count(char_counts)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():
            print(f"{char}: {count}")


if __name__ =="__main__":
    if len(argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        exit(1)
    else:
        file_path = argv[1]
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}")
        main(file_path)
        print("============= END ===============")
        

