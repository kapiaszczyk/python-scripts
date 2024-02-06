import sys
import csv
import markdown
import argparse
from pathlib import Path


def read_markdown_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"File not found at {file_path}")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None


def convert_markdown_to_html(markdown_text):
    try:
        html_content = markdown.markdown(markdown_text)
        return html_content
    except Exception as e:
        print(f"An error occurred while converting Markdown to HTML: {e}")
        return None


def save_file(file_path, content, output_file_path=None):
    # If path to the output directory is passed, save the file there
    # Otherwise save to the directory of the input file
    try:
        if output_file_path is None:
            output_file_path = file_path.replace(".md", "_deck.csv")
        else:
            file_name = Path(file_path).stem
            print(file_name)
            output_file_path = Path(output_file_path).parent / (file_name + "_deck.csv")
        with open(output_file_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerows(content)

        print(f"File created at {(output_file_path).parent} directory")

    except Exception as e:
        print(f"An error occurred while saving the file: {e}")
        return None


def parse_markdown_file(file_path, output_file_path=None):

    # Interpret the heading as question and the rest as the answer
    try:
        markdown_file = read_markdown_file(file_path)
        if markdown_file is None:
            raise Exception("File is empty")

        deck = []
        question = None
        answer = []

        for line in markdown_file.splitlines():
            if line.startswith("###"):
                if question is not None:
                    html_answer = convert_markdown_to_html("\n".join(answer).strip())
                    deck.append([question.strip(), html_answer])
                    answer = []
                question = line[3:].strip()
            else:
                answer.append(line)

        if question is not None:
            html_answer = convert_markdown_to_html("\n".join(answer).strip())
            deck.append([question.strip(), html_answer])

        # Write to the CSV file
        save_file(file_path, deck, output_file_path)

    except Exception as e:
        print(f"An error occurred while parsing the file: {e}")
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
    args = parser.parse_args()
    if args.input:
        print("Path to the file: " + args.input)
        parse_markdown_file(args.input)
    if args.input and args.output:
        print(f"Reading from {args.input}")
        print(f"Saving at {args.output}")
        parse_markdown_file(args.input, args.output)
