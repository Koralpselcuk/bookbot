import sys
from stats import get_num_words, count_characters, sort_character_counts

# Dosya yolunu parametre olarak alan ve dosya içeriğini döndüren fonksiyon
def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Ana fonksiyon
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]

    print("============ BOOKBOT =============")
    print(f"Analyzing book found at {file_path}...")

    try:
        text = get_book_text(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    char_counts = count_characters(text)
    sorted_counts = sort_character_counts(char_counts)

    print("--------- Character Count -------")
    for entry in sorted_counts:
        print(f"{entry['char']}: {entry['count']}")
    
    print("============= END ===============")

# Programı çalıştır
if __name__ == "__main__":
    main()
