<!-- ABOUT  -->
## About 

This is a collection of python scripts that I have written for various purposes.

<!-- GETTING STARTED -->
## Getting Started

To run these scripts, you will need to have python installed on your machine. You can download python from the official website [here](https://www.python.org/downloads/).

<!-- Details-->
## Detailed instructions

### [parse_md_to_anki_csv.py](https://github.com/kapiaszczyk/python-scripts/blob/main/parse_md_to_anki_csv.py)

This script parses markdown notes to a CSV file that can be imported into Anki. The script is designed to work with notes that are formatted in a specific way. The notes should be formatted as follows:

```markdown
### Question
Answer

### Question
Another answer
```

The script will parse the notes and create a CSV file with the following format:

```csv
Question,Answer
Question,Another answer.
```

To use the script, run the following command:

```bash
python parse_notes_to_anki_csv.py -i <input_file> -o [output_file]
```

Where `<input_file>` is the path to the markdown file containing the notes and `<output_file>` is the path to the directory where the CSV file will be saved. If no output file is specified, the CSV file will be saved in the same directory as the input file. 

The script converts the markdown to HTML elements, so the notes can contain HTML tags (e.g. `<br>` for line breaks or `<code>`). It does not support anything more fancy, like images.

### [extract_openapi_paths.py](https://github.com/kapiaszczyk/python-scripts/blob/main/extract_openapi_paths.py)

This script extracts API paths from openAPI v3 documentation. It works with both YAML and JSON files and can output the paths to a simple markdown table.

Usage:
```
python extract_openapi_paths.py -p <path_to_openapi_documentation> -t <True/False> -y <True/False>
```

### [jobboard_data_generation_scripts](https://github.com/kapiaszczyk/python-scripts/tree/main/jobboard_data_generation_scripts)

Scripts that generate test data for one of my personal projects with help of Faker library.

### [create_table_sql_statement.py](https://github.com/kapiaszczyk/python-scripts/blob/main/create_table_sql_statement.py)

Simple script that generates a SQL create table statement. Perfect when for creating table fast. Doesn't support constraints etc.

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
