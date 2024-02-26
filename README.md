# Oxford Dictionary of English Corpus

This repository contains a corpus created from the Oxford Dictionary of English. It includes the original text file of the Oxford English Dictionary, a Python script for parsing the dictionary text, and the resulting corpus in JSON format.

## Contents

- `Oxford English Dictionary.txt` - The original text file of the Oxford Dictionary of English. Obtained from [sujithps/Dictionary on GitHub](https://github.com/sujithps/Dictionary/blob/master/Oxford%20English%20Dictionary.txt).
- `data_parser.py` - A Python script used to extract and parse the text file into a structured format.
- `oxford_corpus.json` - The extracted corpus in JSON format, created using the `data_parser.py` script.

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
    git clone https://github.com/yourusername/your-repository-name.git
    ```
2. Navigate to the repository directory:
    ```
    cd your-repository-name
    ```
3. Open the `data_parser.py` script in a text editor. You will need to modify the script to include the paths to    your local copy of the `Oxford English Dictionary.txt` file and the output path for the `oxford_corpus.json` file. Look for placeholders or comments in the script that indicate where to insert these paths.
4. After updating the file paths, save the script and run it to parse the Oxford English Dictionary text file and generate the JSON corpus:
    ```
    python data_parser.py
    ```
   This will create the `oxford_corpus.json` file at the specified output location.

Please ensure to update the script with the correct file paths on your system before running it.

## Contributing

Contributions to the Oxford Dictionary of English Corpus are welcome! Please feel free to fork the repository, make changes, and submit pull requests.

## License

This project is open-source and available under the [MIT License](LICENSE). The original Oxford English Dictionary text file is obtained from an external source and may be subject to its own terms and conditions.

## Acknowledgments

- Original Oxford English Dictionary text file obtained from [sujithps/Dictionary](https://github.com/sujithps/Dictionary).