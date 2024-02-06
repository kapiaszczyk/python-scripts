<!-- ABOUT  -->
## About 

This is a collection of python scripts that I have written for various purposes.

<!-- GETTING STARTED -->
## Getting Started

To run these scripts, you will need to have python installed on your machine. You can download python from the official website [here](https://www.python.org/downloads/).

### [parse_md_to_anki_csv.py](https://github.com/kapiaszczyk/python-scripts/blob/main/parse_md_to_anki_csv.py)

This script parses markdown notes to a CSV file that can be imported into Anki. The script is designed to work with notes that are formatted in a specific way. The notes should be formatted as follows:

```markdown
### Question
Answer

### Question
Other answer.
```

The script will parse the notes and create a CSV file with the following format:

```csv
Question,Answer
Question,Other answer.
```

To use the script, run the following command:

```bash
python parse_notes_to_anki_csv.py -i <input_file> -o [output_file]
```

Where `<input_file>` is the path to the markdown file containing the notes and `<output_file>` is the path to the directory where the CSV file will be saved. If no output file is specified, the CSV file will be saved in the same directory as the input file. 

The script converts the markdown to HTML elements, so the notes can contain HTML tags (e.g. `<br>` for line breaks or `<code>`).

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
