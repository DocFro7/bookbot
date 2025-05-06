def get_book_text():
    with open("/home/doc/repo/bootdotdev/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
    
    return file_contents

def split_text(contents):
    wordcount = 0
    wordlist = contents.split()

    for word in wordlist:
        wordcount += 1
    
    print(f"{wordcount} words found in the document")

def main(text):
    split_text(text)

main(get_book_text())