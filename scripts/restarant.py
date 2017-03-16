test_data = ['i would like the bill', 'i would like to pay', 'i would like the check', 'can i have the bill', 'can i have the bill', 'can i have the bill', ' no i have you the gym', 'yes can i have the dessert card', 'can i have the dessert card', 'i would like the dessert card', 'i would like the is there card', 'i would like a    ticket to ', ' i dessert menu', 'can i have a   dessert card', 'i would like to the dessert card', 'can i have the dessert menu', 'can i have the dessert menu    *** ', 'can i have the dessert menu', 'can i have the dessert my room', 'can i   have the dessert menu please can i have the dessert menu please', 'can i have the dessert menu', 'can i have the dessert menu', 'can i have the dessert menu pool ', 'can i have the    ***    swimming pool ']


aux_verbs = ['i will buy these', 'i would like an', 'i will have these', 'i want to', "i 'd need a", 'i would like a', 'i will have the', "i 'd like to", 'i would like some', 'i will have an', 'i should like a', 'i will have a', "i 'd like a", 'i should like some', 'i need to', 'i have to', "i 'd want a", "i 'd like some", 'i will take some', 'i should like an', "i 'd like an", 'i should like to', 'i would need a', 'i would want a', 'i would like the', "i 'd like the", 'i will have some', 'i will take the', 'i will take an', 'i will take a', 'i would like to', 'i would need to']
nouns = ['dessert menu', 'bill', 'check']

aux_question_verbs = ['can you tell me', 'can i have a', 'could i have s', 'can you give me', 'can i have the', 'can i buy a', 'can i pay', 'could i have some', 'could you offer me', 'can you bring me', 'could i have an', 'can i have s', 'can i find a', 'could i have a', 'can i buy', 'can i buy some', 'can i have an', 'could you give me', 'can you offer me', 'could i have', 'would you bring me', 'would you give me', 'can you show me', 'could i buy some', 'can i have', 'can i have some', 'could i buy', 'could you tell me', 'can i find the', 'could i buy a', 'could you bring me', 'could i have the', 'can i see the']

def aux_key(sentence):
    for auxkey in sorted(set(aux_verbs), key=len, reverse=True):
        if auxkey in sentence:
            return auxkey
def aux_key_question(sentence):
    for auxkey in sorted(set(aux_question_verbs), key=len, reverse=True):
        if auxkey in sentence:
            return auxkey

def inside_nouns(sentence):
    for nounkey in sorted(set(nouns), key=len, reverse=True):
        if nounkey in sentence:
            return nounkey

reject_words = ['dessert card', 'card']

def accept_restarant(sentence):
    aux = aux_key(sentence)

    if aux == None:
        aux = aux_key_question(sentence)
        if aux:
            sentence = sentence.replace(aux, "")
            nounk = inside_nouns(sentence)
            if nounk:
                sentence = sentence.replace(nounk, "")
                if len(sentence) == 1 or len(sentence) == 0:
                    return True
    if aux:
        sentence = sentence.replace(aux, "")
        nounk = inside_nouns(sentence)
        if nounk:
            sentence = sentence.replace(nounk, "")
            sentence = " ".join(sentence.split(None))
            if len(sentence) == 0:
                return True
    return False

if __name__ == '__main__':

    print(accept_restarant("can i have the dessert menu"))
    print(accept_restarant("can i have the dessert card"))

    if False:
        true = 0
        false = 0
        for pro in test_data:
            sentence = " ".join(pro.split(None))
            if "'" in sentence:
                sentence = sentence.replace("'", " '")

            is_true = accept_restarant(sentence)
            if is_true:
                true +=1
            else:
                false +=1
                print(str(is_true) + "\t" + sentence)

        print("Richtig %s", str(true))
        print("Falsch %s", str(false))
