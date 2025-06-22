def count_words(text):
    word_list = text.split()
    return len(word_list)

def get_book_text(file):
    with open(file) as f:
        return f.read()
    
def get_character_dict(text):
    character_list = list(text)
    character_dict = {}
    for character in character_list:
        if character.lower() not in character_dict:
            character_dict[character.lower()] = 1
        else:
            character_dict[character.lower()] += 1
    return character_dict

def sort_on(items):
    return items["num"]

def dict_list(character_dict):
    dict_list = []
    for key, value in character_dict.items():
        if key.isalpha() == True:
            dict_list.append({"name":key, "num":value})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list