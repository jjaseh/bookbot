def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    characters_dict = {}
    for character in text:
        character = character.lower()
        if character not in characters_dict.keys():
            characters_dict[character] = 1
        else:
            characters_dict[character] += 1
    return characters_dict

def sort_characters(characters):
    characters_dict = []
    for character, count in characters.items():
        character_dict = {
            "char": character,
            "num": count
        }
        characters_dict.append(character_dict)
    characters_dict.sort(reverse=True, key=sort_on)
    return characters_dict

def sort_on(list_of_dicts):
    return list_of_dicts["num"]