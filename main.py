with open("books/frankenstein.txt", "r") as f:
    file_contents = f.read()
    # print(file_contents)

    characters = file_contents.split()

    # print(len(characters))

    characters_dict = {}
    for word in characters:
        for char in word:
            letter = char.lower()
            if letter in characters_dict:
                characters_dict[letter] += 1
            else:
                characters_dict[letter] = 1
    
    # print(characters_dict)
    print("--- Begin report of {f.name} ---")
    print(f"{len(characters)} words found in the document")
    for char in sorted(characters_dict, key=characters_dict.get, reverse=True):
        if char.isalpha():
            print(f"The '{char}' character was found {characters_dict[char]} times")

    print("--- End report ---")