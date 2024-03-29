# Oxford Dictionary of English Corpus

This repository contains a corpus created from the Oxford Dictionary of English. It includes the original text file of the Oxford English Dictionary, a Python script for parsing the dictionary text, and the resulting corpus in JSON format. Each entry in the corpus contains the word, its Part of Speech (POS), and the definition, making it a valuable resource for fine-tuning various models for tasks such as text generation, question answering (QA), classification, and more.

## Contents

- `Oxford English Dictionary.txt` - The original text file of the Oxford Dictionary of English. Obtained from [sujithps/Dictionary on GitHub](https://github.com/sujithps/Dictionary/blob/master/Oxford%20English%20Dictionary.txt).
- `data_parser.py` - A Python script used to extract and parse the text file into a structured format. The script processes each entry to include the word, its Part of Speech (POS), and definition in the JSON format.
- `oxford_corpus.json` - The extracted corpus in JSON format, created using the `data_parser.py` script. The corpus contains detailed entries for each word, including its definition and POS tag.

## Corpus Statistics

- **Total Entries in the Corpus:** 22,879

## Potential Uses

The Oxford Dictionary of English Corpus is versatile and can be used for a variety of computational linguistics and machine learning tasks, including but not limited to:

- **Text Generation**
- **Question Answering (QA)**
- **Text Classification:**
- **And More:**

## Getting Started

To use this repository, you will need Python installed on your system. The `data_parser.py` script is written in Python and is used to generate the JSON corpus from the original text file.

### Prerequisites

- Python 3.x
- The script uses standard libraries that come with Python, including:
  - `json` for parsing and saving the corpus in JSON format.
  - `re` for regular expressions, used in parsing the text file.
  
No additional external libraries are required.

### Usage

1. Clone this repository to your local machine:
    ```
    git clone https://github.com/eneko98/Oxford-Corpus.git
    ```
2. Navigate to the repository directory:
    ```
    cd Oxford-Corpus
    ```
3. Open the `data_parser.py` script in a text editor. You might need to modify the script to include the paths to your local copy of the `Oxford English Dictionary.txt` file and the output path for the `oxford_corpus.json` file. Look for placeholders or comments in the script that indicate where to insert these paths.
4. After updating the file paths, save the script and run it to parse the Oxford English Dictionary text file and generate the JSON corpus:
    ```
    python data_parser.py
    ```
   This will create the `oxford_corpus.json` file at the specified output location.

Please ensure to update the script with the correct file paths on your system before running it.

## Contributing

Contributions to the Oxford Dictionary of English Corpus are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## Acknowledgments

- Original Oxford English Dictionary text file obtained from [sujithps/Dictionary](https://github.com/sujithps/Dictionary).
