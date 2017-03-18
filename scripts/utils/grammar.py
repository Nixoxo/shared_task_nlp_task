import xml.etree.ElementTree as ET
import copy

def create_prompt_response_map(gram):
    prompt_response_map = {}
    for prompt_unit in gram:
        key = None
        responses = []
        for prompt in prompt_unit:
            if prompt.tag == None:
                print("None")
            else:
                if(prompt.tag == 'prompt'):
                    key = prompt.text
                elif(prompt.tag == 'response'):
                    responses.append(prompt.text)
                elif(prompt.tag == 'translated_prompt'):
                    trans_text = prompt.text
                    if "Say you still want:" in trans_text or "(" in trans_text:
                        continue
                    trans_text = trans_text.replace("Ask for: ", "").replace("Say you still want: ", "").replace("Say: ", "").replace("?size", "").replace("?", "")
                    responses.append(trans_text)
        prompt_response_map[key] = responses
    return prompt_response_map

def read_grammar_and_create_map(file):
    tree = ET.parse(file)
    grammar = tree.getroot()
    return create_prompt_response_map(grammar)

def merge_grammars(grammar1, grammar2):
    grammar = copy.deepcopy(grammar1)
    for key in grammar1:
        if key in grammar2:
            for item in grammar2[key]:
                arr = list(grammar[key])
                arr.append(item)
                grammar[key] = arr
            grammar[key] = set(grammar[key])
    return grammar