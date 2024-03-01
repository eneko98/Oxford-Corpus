import json
import re

"""Some of the words have multiple definitions. 
I think this may be a problem if you want to train a model 
as this multiple entries might confuse it.
That's why this further cleaning is made"""

def process_entry(entry):
    parts = re.split(r'(?<=\.)\s(?=\d+\s)', entry['definition'], maxsplit=1)
    cleaned_parts = [part.strip().rstrip('.') for part in parts if part and part.strip()]
    new_entry = {
        "word": entry['word'],
        "pos": entry['pos'],
        "definitions": []
    }

    def remove_leading_number(definition):
        cleaned_definition = re.sub(r'(?<=\))\s1\s', ' ', definition)
        cleaned_definition = re.sub(r'(?<=\w)\s1\s', ' ', cleaned_definition)
        cleaned_definition = re.sub(r'^1\s+', '', cleaned_definition)
        cleaned_definition = re.sub(r'\(\s*1\s*\)\s*', '', cleaned_definition)
        cleaned_definition = re.sub(r'\[\s*1\s*\]\s*', '', cleaned_definition)
        return cleaned_definition.strip()

    if cleaned_parts:
        new_entry['definitions'].append(remove_leading_number(cleaned_parts[0]))

    if len(cleaned_parts) > 1:
        additional_defs = re.split(r'\s(\d+)\s', cleaned_parts[1])
        for i in range(1, len(additional_defs), 2):
            cleaned_definition = remove_leading_number(additional_defs[i + 1])
            new_entry['definitions'].append(cleaned_definition)

    return new_entry

processed_entries = []
pattern = re.compile(r'(\w+)\s+(\w+)\.\s+(.*)')

with open('Oxford English Dictionary.txt', 'r', encoding='utf-8') as file:
    for line in file:
        match = pattern.match(line.strip())
        if match:
            processed_entries.append(process_entry({
                "word": match.group(1),
                "pos": match.group(2),
                "definition": match.group(3)
            }))

with open('oxford_corpus.json', 'w', encoding='utf-8') as outfile:
    json.dump(processed_entries, outfile, indent=4, ensure_ascii=False)