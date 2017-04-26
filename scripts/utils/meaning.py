import scripts.utils.nlp_utils as nlp

def is_slice_in_list(s, l):
    len_s = len(s)  # so we don't recompute length of s on every iteration
    return any(s == l[i:len_s + i] for i in range(len(l) - len_s + 1))


def is_slice_in_list2(s, l):
    len_s = len(s)  # so we don't recompute length of s on every iteration
    for i in range(len(l) - len_s + 1):
        if s == l[i:len_s + i]:
            return i


def extract_by_pattern(patterns, tags, words):
    extracted_words = []
    tags_string = " ".join(tags)
    for pattern in patterns:
        pattern_string = " ".join(pattern)
        if is_slice_in_list(pattern, tags):
            pattern_start_index = is_slice_in_list2(pattern, tags)
            if len(pattern) > 1:
                # pattern_end_index = tags.index(pattern[-1], pattern_start_index+1)
                pattern_end_index = pattern_start_index + len(pattern) - 1
                if pattern_end_index - pattern_start_index + 1 == len(pattern):
                    extracted_part = ""
                    for i in range(pattern_start_index, pattern_end_index + 1):
                        extracted_part += words[i] + " "
                    extracted_words.append(extracted_part[:-1])
            else:
                extracted_words.append(words[pattern_start_index])
            """
            if len(pattern) > 1:
                pattern_end_index = tags.index(pattern[-1], pattern_start_index+1)
                if pattern_end_index - pattern_start_index +1 != len(pattern):
                    pattern_end_index = tags.index(pattern[-1], pattern_end_index+1)

                if pattern_end_index - pattern_start_index + 1 == len(pattern):
                    extracted_part = ""
                    for i in range(pattern_start_index, pattern_end_index+1):
                        extracted_part += words[i] + " "


                    extracted_words.append(extracted_part[:-1])
            else:
                extracted_words.append(words[pattern_start_index])
            """
    return extracted_words


def extract_key_dt_nouns(nlp_sent):
    tags = nlp_sent[2]
    words = nlp.spacy_words_to_string_array(nlp_sent[0])
    sentence = " ".join(words)
    # words = " ".join(nlp_sent[0])
    # [['DT', 'NN', 'NN']]
    prio_one_patterns = [['DT', 'NN', 'NN'], ['DT', 'NN', 'NNS'],
                         ['DT', 'NN']]

    extracted_words = extract_by_pattern(prio_one_patterns, tags, words)
    return extracted_words


def extract_key_nouns(nlp_sent):
    tags = nlp_sent[2]
    words = nlp.spacy_words_to_string_array(nlp_sent[0])
    sentence = " ".join(words)
    # words = " ".join(nlp_sent[0])
    # [['DT', 'NN', 'NN']]
    prio_one_patterns = [['PRP$', 'NN', 'NN'], ['PRP$', 'NN', 'NNS'], ['PRP$', 'NNS', 'NNS'], \
                         ['PRP$', 'NN'], ['PRP$', 'NNS'], ['NN', 'NNS'], ['NN', 'NN'], ['RB', 'NN'], ['JJ', 'NNS'], \
                         ['JJ', 'NN'], ['CD', 'NN'], ['CD', 'NNS'], ['NN'], ['NNS']]

    # Only when no prio_one_pattern fits
    prio_sec_patterns = [['NN'], ['NNS']]
    extracted_words = extract_by_pattern(prio_one_patterns, tags, words)
    if len(extracted_words) < 1:
        extracted_words = extract_by_pattern(prio_sec_patterns, tags, words)
    return extracted_words


def generate_dt_nouns_by_key_nouns(nlp_nouns):
    # FIX ME a credit cards does work
    dts = ['a', 'the']
    patterns = [['NN', 'NN'], ['NN', 'NNS'], ['NN']]
    tags = nlp_nouns[2]
    words = nlp.spacy_words_to_string_array(nlp_nouns[0])

    generated_words = []
    for pattern in patterns:
        if pattern == tags:
            for dt in dts:
                sentence = dt + " " + " ".join(words)
                generated_words.append(sentence)
    return generated_words


def generalise_aux_verb(nlp_sent):
    tags = nlp_sent[2]
    words = nlp.spacy_words_to_string_array(nlp_sent[0])
    sentence = " ".join(words)
    patterns = [['PRP', 'MD', 'VB', 'TO'], ['PRP', 'MD', 'VB', 'DT'], ['PRP', 'VBP', 'TO']]

    extracted_words = extract_by_pattern(patterns, tags, words)
    return extracted_words


def create_meaning_map(grammar):
    prompt_noun_map = {}
    for prompt in grammar:
        try:
            extracted_nouns = []
            for response in grammar[prompt]:
                nlp_s = nlp.nlp_sentence(response)
                nouns = extract_key_nouns(nlp_s)
                if len(nouns) > 0:
                    extracted_nouns.extend(nouns)
            prompt_noun_map[prompt] = list(set(extracted_nouns))
        except:
            print("error")
            print(prompt)
    return prompt_noun_map


def meaning_is_correct(prompt_noun_map, prompt_unit, transcript, clear_transcript, unique_sentence):
    nlp_transcript = nlp.nlp_sentence(transcript)
    nlp_clear = nlp.nlp_sentence(transcript)
    nlp_unqiue = nlp.nlp_sentence(unique_sentence)
    extracted_nouns_t = extract_key_nouns(nlp_transcript)
    extracted_nouns_c = extract_key_nouns(nlp_clear)
    extracted_nouns_u = extract_key_nouns(nlp_unqiue)

    for noun in extracted_nouns_t:
        try:
            if noun in prompt_noun_map[prompt_unit]:
                return True
        except:
            print(prompt_unit)
            print(prompt_noun_map[prompt_unit])
            print(noun)
    for noun in extracted_nouns_c:
        if noun in prompt_noun_map[prompt_unit]:
            return True
    for noun in extracted_nouns_u:
        if noun in prompt_noun_map[prompt_unit]:
            return True
    return False