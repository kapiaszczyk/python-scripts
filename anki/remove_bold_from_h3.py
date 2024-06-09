"""Parse Markdown to Anki CSV deck.

This script parses Markdown notes containing question and answer pairs
and converts them into a CSV file that can be imported into Anki as a deck.

"""

import argparse
import logging


def read_markdown_file(file_path):
    """Reads the markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")


def resolve_output_path(file_path):
    """Resolves the output file path."""
    return file_path.replace(".md", "_removed.md")


def save_file(file_path, content):
    """Writes the parsed content to a file."""

    output_file_path = resolve_output_path(file_path)

    try:
        with open(output_file_path, "w", newline="", encoding="utf-8") as file:
            file.write(content)
            logger.info(f"File saved at {output_file_path}")
    except Exception as e:
        logger.error(f"An error occurred while saving the file: {e}")
        return None
    

def remove_asterisks(line):
    """Remove double asterisks from the text."""
    return line.replace('**', '')


def remove_bold(file_path):
    """Removes bold formatting from the headers."""

    try:
        content = read_markdown_file(file_path)
        modified_lines = []

        for line in content.splitlines():
            if line.startswith("###"):
                line = remove_asterisks(line)
            modified_lines.append(line)

        modified_content = "\n".join(modified_lines)
        save_file(file_path, modified_content)

    except Exception as e:
        logger.error(f"An error occurred while parsing the file: {e}")
        return None


def setup_logging():
    """Setup logging configuration."""
    logging.basicConfig(level=logging.INFO, format="%(levelname)s - %(message)s")
    return logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--input", "-i", help="path to the markdown file", required=True)
    args = parser.parse_args()

    logger = setup_logging()

    remove_bold(args.input)
