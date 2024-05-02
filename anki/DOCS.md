# Parse Markdown to Anki CSV

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

## Usage

To use the script, run the following command:

```bash
python parse_notes_to_anki_csv.py -i <input_file> -o [output_file]
```

Where `<input_file>` is the path to the markdown file containing the notes and `<output_file>` is the path to the directory where the CSV file will be saved. If no output file is specified, the CSV file will be saved in the same directory as the input file. 

The script converts the markdown to HTML elements, so the notes can contain HTML tags (e.g. `<br>` for line breaks or `<code>`). It does not support anything more fancy, like images. It also removes the `<p>` tags from the output.

## Logging

The script supports logging. Use the `--log` flag to enable console logging and the `--log_level` flag to set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL).
