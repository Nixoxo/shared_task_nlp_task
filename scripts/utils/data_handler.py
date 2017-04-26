from scripts.utils.string_handling import *


def transcript_processed_unique(transcript):
    sentence = transcript
    if "***" in sentence:
        sentence = sentence.replace("***", "")
    processed = sentence
    processed = clear_sentence(sentence).lstrip()
    unique_sentence = get_unique_sentence(processed).lstrip()
    return processed, unique_sentence

def read_test_data(file):
    with open(file, 'r') as reader:
        test_data = reader.readlines()
        prompt_map = {}
        for item in test_data[1:]:
            split = item.replace("\n", "").split("\t")
            prompt = split[1]
            transcript = split[3]
            processed, unique_sentence = transcript_processed_unique(split[3])
            response = {
                'id':split[0],
                'transcript':transcript,
                'processed':processed,
                'unique':unique_sentence,
                'language':False,
                'meaning':False,
                'judgement':'reject'
            }
            if prompt in prompt_map:
                prompt_map[prompt].append(response)
            else:
                arr = []
                arr.append(response)
                prompt_map[prompt] = arr

        return prompt_map

def get_test_data_by_prompts(cluster_prompts, test_data, grammar):
    # Hole alle Daten mit den prompts
    transcripts_arr = []
    for key in cluster_prompts:
        for response in test_data[key]:
            if response['transcript'] not in grammar[key]:
                transcripts_arr.append(response['transcript'])
    #for key in arr:
    #    if arr[]
    #    transcripts_arr.append()
    return transcripts_arr

def get_test_data_by_false_prompts(cluster_prompts, false_prompts, grammar):
    # Hole alle Daten mit den prompts
    transcripts_arr = {}
    for key in cluster_prompts:
        if key in false_prompts:
            transcripts_arr[key] =[]
            for response in false_prompts[key]:
                if response['transcript'] not in grammar[key]:
                    transcripts_arr[key].append(response)
    #for key in arr:
    #    if arr[]
    #    transcripts_arr.append()
    return transcripts_arr

def read_reference(file):
    id_map = {}
    with open(file, 'r') as reader:
        lines = reader.readlines()[1:]
        for line in lines:
            split = line.replace("\n", "").split("\t")
            id_ = split[0]
            prompt = split[1]
            transcript = split[3]
            language_string = split[4]
            meaning_string = split[5]
            language = False
            meaning=False
            if language_string == 'correct':
                language = True
            if meaning_string == 'correct':
                meaning = True

            item = {
                'id': id_,
                'prompt': prompt,
                'transcript': transcript,
                'language': language,
                'meaning': meaning
            }
            id_map[id_] = item
    return id_map