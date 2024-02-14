import sys
import csv
import markdown
import argparse
import re
import logging
from pathlib import Path


def read_markdown_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except Exception as e:
        logger.error(f"An error occurred while reading the file: {e}")
        raise e


def convert_markdown_to_html(markdown_text):
    try:
        html_content = markdown.markdown(markdown_text, extensions=['fenced_code'])
        return html_content
    except Exception as e:
        logger.error(f"An error occurred while converting Markdown to HTML: {e}")
        return None


def save_file(file_path, content, output_file_path=None):
    # If path to the output directory is passed, save the file there
    # Otherwise save to the directory of the input file
    try:
        if output_file_path is None:
            output_file_path = file_path.replace(".md", "_deck.csv")
        else:
            file_name = Path(file_path).stem
            output_file_path = Path(output_file_path) / (file_name + "_deck.csv")
        with open(output_file_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(content)
            logger.info(f"File saved at {output_file_path}")

    except Exception as e:
        logger.error(f"An error occurred while saving the file: {e}")
        return None


def parse_markdown_file(file_path, output_file_path=None):

    # Interpret the heading as question and the rest as the answer
    # Skip '#' headings
    try:
        try:
            markdown_file = read_markdown_file(file_path)
        except Exception as e:
            return None
           
        deck = []
        question = None
        answer = []

        for line in markdown_file.splitlines():
            if line.startswith("# "):
                continue
            if line.startswith("###"):
                if question is not None:
                    html_answer = convert_markdown_to_html("\n".join(answer).strip())
                    html_answer = re.sub(r'<\/?p>', '', html_answer)
                    deck.append([question.strip(), html_answer])
                    answer = []
                question =  re.sub(r'<\/?p>', '', convert_markdown_to_html(line[3:].strip()))
            else:
                answer.append(line)

        if question is not None:
            html_answer =  re.sub(r'<\/?p>', '', convert_markdown_to_html("\n".join(answer).strip()))
            deck.append([question.strip(), html_answer])

        save_file(file_path, deck, output_file_path)

    except Exception as e:
        logger.error(f"An error occurred while parsing the file: {e}")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Python script for turning markdown notes into flashcards in CSV format"
    )
    parser.add_argument(
        "--input", "-i", help="path to the markdown file", action="store"
    )
    parser.add_argument(
        "--output", "-o", nargs="?", help="path to the output directory", action="store"
    )
    parser.add_argument(
        "--log", "-l", help="enable console logging", action='store_true'
    )
    parser.add_argument(
        "--log_level", "-lv", help="logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)", default="INFO"
    )
    args = parser.parse_args()
    
    log_format = "%(levelname)s - %(message)s"
    logging.basicConfig(level=logging.CRITICAL, format=log_format)
    logger = logging.getLogger(__name__)
    
    if args.log and args.log in ["True", "true", "1"]:
        logger.addHandler(logging.StreamHandler(sys.stdout))
    if args.log_level and args.log_level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"] and args.log:
        logger.setLevel(args.log_level)
    if args.input and not args.output:
        parse_markdown_file(args.input)
    elif args.input and args.output:
        parse_markdown_file(args.input, args.output)
