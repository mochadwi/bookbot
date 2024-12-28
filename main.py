with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    print(file_contents)

    characters = file_contents.split()

    print(len(characters))

    characters_dict = {}
    for word in characters:
        for char in word:
            letter = char.lower()
            if letter in characters_dict:
                characters_dict[letter] += 1
            else:
                characters_dict[letter] = 1
    
    print(characters_dict)