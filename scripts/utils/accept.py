def accept_meaning(key_nouns_of_prompt_cluster, key_nouns_of_prompts, response):
    transcript, processed, unique = response['transcript'], response['processed'], response['unique']

    key_nouns_state = False
    prompt_state = False
    for key_noun in key_nouns_of_prompt_cluster:
        if key_noun in transcript or key_noun in processed or key_noun in unique:
            key_nouns_state = True
            break
    for key_noun in key_nouns_of_prompts:
        if key_noun in transcript or key_noun in processed or key_noun in unique:
            prompt_state = True
            break

    return key_nouns_state & prompt_state

def inside(prompt, map_of_prompts):
    if prompt in map_of_prompts:
        return True
    return False