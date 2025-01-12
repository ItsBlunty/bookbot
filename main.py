def main():
    bookpath = "books/frankenstein.txt"
    booktext = getbooktext(bookpath)
    wordcount = getwordcount(booktext)
    characters = getcharactercount(booktext)
    print(characters)

def getwordcount(text):
    words = text.split()
    return len(words)

def getcharactercount(text):
    charactercount = {}
    lowercasetext = text.lower()
    lowernospace = lowercasetext.replace(" ","")
    for character in lowernospace:
        if character in charactercount:
            charactercount[character] += 1
        else:
            charactercount[character] = 1
    return charactercount

def getbooktext(booklocation):
    with open(booklocation) as f:
        return f.read()

main()