import json
import re

entries = []

with open('', 'r') as file:
    for line in file:
        match = re.match(r'(\w+)\s+(\w+)\.\s+(.*)', line)
        if match:
            word, pos, definition = match.groups()
            entry = {
                "word": word,
                "pos": pos,
                "definition": definition
            }
            entries.append(entry)

#Paths are deleted by default. You will need to add your own paths.
            
with open('', 'w') as json_file:
    json.dump(entries, json_file, indent=4)

#Further cleaning of the corpus (unicode and strange characters)
with open('', 'r', encoding='utf-8') as file:
    corpus = json.load(file)

for entry in corpus:
    entry['definition'] = entry['definition'].encode('utf-8').decode('unicode-escape').replace('\u007f', '')

with open('', 'w', encoding='utf-8') as file:
    json.dump(corpus, file, ensure_ascii=False, indent=4)