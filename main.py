def main():
    with open("books/frankenstein.txt") as f:
        book_content = f.read()
        words = book_content.split()
        lowered_string = book_content.lower()
        chars = {}
        for char in lowered_string:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 0
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        for key in chars:
            if key.isalpha():
                print(f"The '{key}' character was found {chars[key]} times")
        print("--- End report ---")

main()