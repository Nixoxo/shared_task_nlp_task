import copy

k = 3


def two_digits(x):
    if x == 'undefined':
        return 'undefined'
    else:
        return ("%.2f" % x)


def three_digits(x):
    if x == 'undefined':
        return 'undefined'
    else:
        return ("%.3f" % x)


def print_scores(scores):
    CA = scores['CorrectAccept']
    GFA = scores['GrossFalseAccept']
    PFA = scores['PlainFalseAccept']
    CR = scores['CorrectReject']
    FR = scores['FalseReject']

    FA = PFA + k * GFA
    Correct = CA + FR
    Incorrect = CR + GFA + PFA
    Z = Correct + Incorrect

    if (CR + FA) > 0:
        IncorrectRejectionRate = CR / (CR + FA)
    else:
        IncorrectRejectionRate = 'undefined'

    if (FR + CA) > 0:
        CorrectRejectionRate = FR / (FR + CA)
    else:
        CorrectRejectionRate = 'undefined'

    if (CorrectRejectionRate != 'undefined' and IncorrectRejectionRate != 'undefined'):
        D = IncorrectRejectionRate / CorrectRejectionRate
    else:
        D = 'undefined'

    if (CA + FA) > 0:
        Precision = CA / (CA + FA)
    else:
        Precision = 'undefined'

    if (CA + FR) > 0:
        Recall = CA / (CA + FR)
    else:
        Recall = 'undefined'

    if (Precision != 'undefined' and Recall != 'undefined'):
        F = (2 * Precision * Recall) / (Precision + Recall)
    else:
        F = 'undefined'

    if (Z > 0):
        SA = (CA + CR) / Z
    else:
        SA = 'undefined'

    print('\nINCORRECT UTTERANCES (' + str(Incorrect) + ')')
    print('CorrectReject    ' + str(CR))
    print('GrossFalseAccept ' + str(GFA) + '*' + str(k) + ' = ' + str(GFA * k))
    print('PlainFalseAccept ' + str(PFA))
    print('RejectionRate    ' + three_digits(IncorrectRejectionRate))

    print('\nCORRECT UTTERANCES (' + str(Correct) + ')')
    print('CorrectAccept    ' + str(CA))
    print('FalseReject      ' + str(FR))
    print('RejectionRate    ' + three_digits(CorrectRejectionRate))

    print('\nMEASURES')
    print('Precision        ' + three_digits(Precision))
    print('Recall           ' + three_digits(Recall))
    print('F-measure        ' + three_digits(F))
    print('Scoring accuracy ' + three_digits(SA))
    print('D                ' + three_digits(D))


default_scores = {'CorrectAccept': 0, 'GrossFalseAccept': 0, 'PlainFalseAccept': 0, 'CorrectReject': 0,
                  'FalseReject': 0}


def score_decision(decision, language_correct_gs, meaning_correct_gs, this_score):
    if ( decision == 'accept' and language_correct_gs == 'correct' ):
        result = 'CorrectAccept'
    elif ( decision == 'accept' and meaning_correct_gs == 'incorrect' ):
        result = 'GrossFalseAccept'
    elif ( decision == 'accept' ):
        result = 'PlainFalseAccept'
    elif ( decision == 'reject' and language_correct_gs == 'incorrect' ):
        result = 'CorrectReject'
    else:
        result = 'FalseReject'
    this_score[result] = this_score[result] + 1
    return result, this_score


def read_gold_standard():
    id_map = {}
    file = "referencetest_final.csv"
    with open(file, 'r') as reader:
        data = reader.readlines()[1:]
        for item in data:
            items = item.replace("\n", "").split("\t")
            id_ = items[0]
            language = items[4]
            meaning = items[5]
            id_map[id_] = {"language": language, "meaning": meaning}
    return id_map


gold_standard_map = read_gold_standard()


def get_single_results(some_score_map):
    CorrectAccept = []
    GrossFalseAccept = []
    PlainFalseAccept = []
    CorrectReject = []
    FalseReject = []
    for id_ in some_score_map:
        item = some_score_map[id_]
        result = item['result']

        if result == 'CorrectAccept':
            CorrectAccept.append(id_)
        elif result == 'GrossFalseAccept':
            GrossFalseAccept.append(id_)
        elif result == 'PlainFalseAccept':
            PlainFalseAccept.append(id_)
        elif result == 'CorrectReject':
            CorrectReject.append(id_)
        elif result == 'FalseReject':
            FalseReject.append(id_)
        else:
            print("Something went wrong")
            break

    return (CorrectAccept, GrossFalseAccept, PlainFalseAccept, CorrectReject, FalseReject)


"""
Excepts map with id and judgement
"""
def score_data(id_judgement_map):
    this_score = None
    this_score = copy.deepcopy(default_scores)
    score_map = {}
    for id_ in id_judgement_map:
        if id_ not in gold_standard_map:
            print("Some id is not in gs map")
            break

        decision = id_judgement_map[id_]

        language_correct = gold_standard_map[id_]['language']
        meaning_correct = gold_standard_map[id_]['meaning']
        result, this_score = score_decision(decision, language_correct, meaning_correct, this_score)
        score_map[id_] = {
            "decision": decision,
            "language": language_correct,
            "meaning": meaning_correct,
            "result": result
        }
    return score_map, this_score


def read_abgabe_file(file):
    id_map = {}
    with open(file, 'r') as reader:
        data = reader.readlines()[1:]
        for item in data:
            items = item.replace("\n", "").split("\t")
            id_ = items[0]
            judgement = items[3]
            id_map[id_] = judgement
    return id_map


"""
v11_data = read_abgabe_file('v11Abgabe.csv')
score_map, v11scores = score_data(v11_data)
print_scores(v11scores)
"""