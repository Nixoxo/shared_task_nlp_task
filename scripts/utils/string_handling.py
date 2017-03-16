def remove_whitespace(string):
    return " ".join(string.split(None))

abbreviation_map = {"don't": "do not",
                    "haven't": "have not",
                    "i'd": "i would",
                    "i'm": "i am",
                    "isn't": "is not",
                    "it's": "it is",
                    "o'clock": "o'clock",
                    "that's": "that is",
                    "there's": "there is"}

def remove_abbreviations(sentence, abbreviations=abbreviation_map):
    trans_sentence = ""
    words = sentence.split(" ")
    for word in words:
        if word in abbreviations:
            word = abbreviations[word]
        trans_sentence += word + " "

    return trans_sentence[:-1]

remove_words_list = ["yes", "thanks", "thank you", "please", "also"]

def remove_words_by_list(sentence, remove_words=remove_words_list):
    words = sentence.split(" ")
    trans_sentence = ""
    # Remove no at begin
    if words[0] == "no":
        words = words[1:]

    # Remove no at end
    if words[-1] == "no":
        words = words[:-1]

    for word in words:
        if word not in remove_words:
            trans_sentence += word + " "
    return trans_sentence

def clear_sentence(sentence, remove_words=remove_words_list, abbreviations=abbreviation_map):
    sentence = remove_whitespace(sentence)
    sentence = remove_words_by_list(sentence, remove_words)
    sentence = remove_whitespace(sentence)
    sentence = remove_abbreviations(sentence, abbreviations)
    return sentence

def get_unique_sentence(sentence):
    trans_sentence = ""
    dict_words = {}
    words = sentence.split(" ")
    for word in words:
        if word in dict_words:
            continue
        dict_words[word] = 1
        trans_sentence += word + " "
    return trans_sentence[:-1]

if __name__ == '__main__':
    print(remove_words_by_list(remove_abbreviations("no I do not no know")))
    print(remove_words_by_list(remove_abbreviations("no I do not no know no")))
    print(remove_words_by_list(remove_abbreviations("I do not no know no")))

    print(get_unique_sentence("I do not no no no know no"))