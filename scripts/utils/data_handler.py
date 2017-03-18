def read_test_data(file):
    with open(file, 'r') as reader:
        test_data = reader.readlines()
        prompt_map = {}
        for item in test_data[1:]:
            split = item.replace("\n", "").split("\t")
            prompt = split[1]

            if prompt in prompt_map:
                prompt_map[prompt].append({'id': split[0], "transcript": split[3]})
            else:
                arr = []
                arr.append({'id': split[0], "transcript": split[3]})
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