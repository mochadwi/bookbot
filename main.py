with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    print(file_contents)

    characters = file_contents.split()

    print(len(characters))