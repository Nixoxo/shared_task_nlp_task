import scripts.utils.accept as accept
zimmer_prompts = [
    "Frag: Zimmer für 1 Woche",
    "Frag: Zimmer für 2 Nächte",
    "Frag: Zimmer für 3 Nächte",
    "Frag: Zimmer für 4 Nächte",
    "Frag: Zimmer für 5 Nächte",
    "Frag: Zimmer für 6 Nächte",
    "Frag: Zimmer für 7 Nächte"]

zimmer_key_nouns = ['hotel', 'hotel room', 'room']

zimmer_map = {
    "Frag: Zimmer für 1 Woche": ['one week', 'week'],
    "Frag: Zimmer für 2 Nächte": ['two nights'],
    "Frag: Zimmer für 3 Nächte": ['three nights'],
    "Frag: Zimmer für 4 Nächte": ['four nights'],
    "Frag: Zimmer für 5 Nächte": ['five nights'],
    "Frag: Zimmer für 6 Nächte": ['six nights'],
    "Frag: Zimmer für 7 Nächte": ['seven nights']
}

def get_prompts():
    return zimmer_prompts

def inside_zimmer_prompts(prompt):
    return accept.inside(prompt, zimmer_map)

def accept_zimmer(prompt, response):
    return accept.accept_meaning(zimmer_map[prompt], zimmer_key_nouns, response)

if __name__ == '__main__':
    print(inside_zimmer_prompts("Frag: Zimmer für 1 Woche"))
    print(inside_zimmer_prompts("Frag: Not für 1 Woche"))