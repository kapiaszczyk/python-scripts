"""Parse Markdown to Anki CSV deck.

This script parses Markdown notes containing question and answer pairs
and converts them into a CSV file that can be imported into Anki as a deck.

"""

import sys
import csv
import markdown
import argparse
import re
import logging
from pathlib import Path


def read_markdown_file(file_path):
    """Reads the markdown file."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")


def convert_markdown_to_html(markdown_text):
    """Converts Markdown syntax to HTML tags."""
    try:
        return markdown.markdown(markdown_text, extensions=['fenced_code'])
    except Exception as e:
        logger.error(f"Error converting Markdown to HTML: {e}")
        return None


def resolve_output_path(file_path, output_file_path):
    """Resolves the output file path."""
    if output_file_path is None:
        return file_path.replace(".md", "_deck.csv")
    else:
        return Path(output_file_path) / (Path(file_path).stem + "_deck.csv")


def save_file(file_path, content, output_file_path=None):
    """Writes the parsed content to a file."""

    output_file_path = resolve_output_path(file_path, output_file_path)

    try:
        with open(output_file_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(content)
            logger.info(f"File saved at {output_file_path}")
    except Exception as e:
        logger.error(f"An error occurred while saving the file: {e}")
        return None
    

def drop_empty_lines(text):
    """Remove empyt lines from the file."""

    lines = [line for line in text.splitlines() if line.strip() != ""]
    return "\n".join(lines)


def parse_markdown_file(file_path, output_file_path=None):
    """Parses markdown file by extracting question and answer pairs."""

    logger.info("Parsing markdown file: " + file_path)

    try:
        markdown_file = drop_empty_lines(read_markdown_file(file_path))

        deck = []
        question = None
        answer = []

        for line in markdown_file.splitlines():
            if line.startswith("# "):
                continue
            if line.startswith("###"):
                if question is not None:
                    html_answer = convert_markdown_to_html(
                        "\n".join(answer).strip())
                    deck.append([re.sub(r'</?p>', '', question.strip()), re.sub(r'</?p>', '', html_answer)])
                    answer = []
                question = convert_markdown_to_html(line[3:].strip())
            else:
                answer.append(line)

        if question is not None:
            html_answer = convert_markdown_to_html("\n".join(answer).strip())
            deck.append([question.strip(), html_answer])

    except Exception as e:
        logger.error(f"An error occurred while parsing the file: {e}")
        return None

    save_file(file_path, deck, output_file_path)


def setup_logging(log_level=logging.INFO):
    """Setup logging configuration."""
    logging.basicConfig(level=log_level, format="%(levelname)s - %(message)s")
    return logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert Markdown notes to Anki CSV deck")
    parser.add_argument("--input", "-i", help="path to the markdown file", required=True)
    parser.add_argument("--output", "-o", help="path to the output CSV file (default: input_deck.csv)")
    parser.add_argument("--log", "-l", help="enable console logging", action='store_true')
    parser.add_argument("--log_level", "-lv", help="logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)",
                        default="INFO")
    args = parser.parse_args()

    logger = setup_logging(log_level=getattr(logging, args.log_level.upper()))

    if args.log:
        logger.addHandler(logging.StreamHandler(sys.stdout))

    parse_markdown_file(args.input, args.output)
