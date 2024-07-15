def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(count_char_count(text=text))
    print_book_report(book_path,count_words_in_book(text),count_char_count(text=text))


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_book(text):
    words = text.strip().split()
    return len(words)

def count_char_count(text):
    char_count = {}
    text = text.lower().strip()
    for i in text:
        if i!= ' ':
            if i not in char_count:
                char_count[i] = 1
            elif i in char_count:
                char_count[i] += 1
    return char_count

def print_book_report(path,word_count,char_c):
    print(f"--- Begin report of {path}")
    print(f"{word_count} words found in the document")
    for k,v in char_c.items():
        print(f"The '{k}' character was found {v} times")


main()