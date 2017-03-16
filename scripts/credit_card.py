# Grob Implementierte Regel
# AUX | VERB_PREP | NN\ NNS

# Test data sind die, die nicht in Reference Grammar drin sind
test_prompts = ["Sag: Ich möchte mit Dollars bezahlen",
"Sag: Ich möchte mit Euros bezahlen",
"Sag: Ich möchte mit Kreditkarte bezahlen",
"Sag: Ich möchte mit Mastercard bezahlen",
"Sag: Ich möchte mit Postkarte bezahlen",
"Sag: Ich möchte mit Visa bezahlen",
"Sag: Ich möchte mit Pfund bezahlen",
"Sag: Ich möchte mit Schweizer Franken bezahlen"]

nouns = ['card', 'credit card', 'pounds', 'mastercard', 'visa', 'francs', 'dollars', 'cards', 'master card', 'euros', 'credit cards', 'post card']
question_verbs = ['is it possible to pay', 'do you accept', 'can i pay with', 'can i pay', 'can i pay by']
verbs = ['would like to pay with', 'would like to pay by']

#aux_verbs = ['i should like to', 'i have to', 'i want to', "i 'd like to", 'i would like to', 'i need to', 'i would need to']
aux_verbs = ['i will buy these', 'i would like an', 'i will have these', 'i want to', "i 'd need a", 'i would like a', 'i will have the', "i 'd like to", 'i would like some', 'i will have an', 'i should like a', 'i will have a', "i 'd like a", 'i should like some', 'i need to', 'i have to', "i 'd want a", "i 'd like some", 'i will take some', 'i should like an', "i 'd like an", 'i should like to', 'i would need a', 'i would want a', 'i would like the', "i 'd like the", 'i will have some', 'i will take the', 'i will take an', 'i will take a', 'i would like to', 'i would need to']
verb_prep = ['am from', 'talk with', 'pay with', 'go on', 'speak with', 'wait for', "'m on", 'sit in', 'talk to', 'speak to', 'am on', 'pay by', 'leave on']
verb_det = ['like the', 'want some', 'are the', 'want an', 'need a', 'take an', 'have a', 'go thursday', 'find any', 'have these', 'do these', 'want this', 'am an', 'do the', 'like some', 'want a', 'take some', 'go this', 'take a', 'find the', 'am a', 'have some', 'get a', 'find a', 'want these', 'take the', 'need an', 'are these', 'like an', 'need some', 'buy these', 'see the', 'have the', 'buy some', 'like a', 'buy a', 'want the', 'have an']


def aux_key(sentence):
    for auxkey in sorted(set(aux_verbs), key=len, reverse=True):
        if auxkey in sentence:
            return auxkey

def aux_key_question(sentence):
    for auxkey in sorted(set(question_verbs), key=len, reverse=True):
        if auxkey in sentence:
            return auxkey

def verb_prep_key(sentence):
    for verbprepkey in sorted(set(verb_prep), key=len, reverse=True):
        if verbprepkey in sentence:
            return verbprepkey


def inside_nouns(sentence):
    for nounkey in sorted(set(nouns), key=len, reverse=True):
        if nounkey in sentence:
            return nounkey


def accept_credit_card(sentence):
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
        verb_prep = verb_prep_key(sentence)
        if verb_prep:
            sentence = sentence.replace(verb_prep, "")
            sentence = " ".join(sentence.split(None))
            nounk = inside_nouns(sentence)
            if nounk:
                sentence = sentence.replace(nounk, "")
                if len(sentence) == 0:
                    return True
    return False

def test_data_prompts():
    test_data = ['can i buy by post ', 'i would to pay by dollars', 'i would pay with euros', 'can i   am a    room', 'my',
     'i want to pay with credit card', 'i want to pay with by credit card', 'i want to pay with  ***  credit card',
     ' i would like pay with by credit card', 'i would to pay by credit card', 'i would to pay by credit card',
     'i would to pay pay by credit card', 'i would pay by credit card', 'i   ***  would pay with credit card',
     'i want where is the credit card', 'i would pay with credit card', 'i would like pay with the credit card',
     'i want pay with credit card', 'i want pay with credit card', 'i like to buy with credit card',
     'i like to pay by credit card', 'i like to pay with credit card', 'i like to pay with credit card',
     'can i  ***  will credit card', " i don't note", 'can i   am a pay by mastercard',
     'can i pay by    ***   mastercard', 'i would like to pay with my    ***   mastercard',
     'i   ***    ***  pay with mastercard', '***   ***   ***     ***  ', 'i would like to pay with master card   ',
     'can i pay by    ***   mastercard', 'i want to buy with    ***   mastercard', 'can i pay with leave at card   ',
     'i want pay with is the mastercard', 'can i pay be mastercard', 'can i  ***   my mastercard',
     'i want to pay with my post card', 'i would like to pay with by post card', 'i would like to pay with',
     'i want pay', 'i want to pay with credit card', 'i would like to pay by master card',
     "i'd like to pay with post card", 'i would pay with post card', 'i like  ***  pay with post card',
     '***   can i   am by post card', 'i would like  ***  ***   pay visa', 'i would like to pay  ***  visa',
     'i would like to  ***   pay visa', 'can i pay with  ***  visa', 'i want to pay by visa', 'i would to pay by visa',
     'i go pay with green park', 'pay with visa', 'i want pay with visa card', 'i want pay with visa',
     'i want pay with visa', 'can i pay with visa visa', 'can i pay by card', 'can i pay by card', "pay a i'd like pommes",
      "i'd like  ***  tickets with pounds", 'can i pay with bar ', 'can i pay with euro ', 'i like  ***  buy with pounds', 'i would like to pay with master with master card', 'i would like to pay by have from france', 'can i  ***   am from france', '***   can i   i buy three nights', 'i like i   with swiss francs']
    return test_data

if __name__ == '__main__':

    print(accept_credit_card("can i pay by card"))
    """
    credit_test_prompts = test_data_prompts()
    true = 0
    false = 0
    for pro in credit_test_prompts:
        sentence = " ".join(pro.split(None))
        if "'" in sentence:
            sentence = sentence.replace("'", " '")

        is_true = accept_credit_card(sentence)
        if is_true:
            true +=1
        else:
            false +=1
        print(str(is_true) + "\t" + sentence)

    print("Richtig %s", str(true))
    print("Falsch %s", str(false))

    """