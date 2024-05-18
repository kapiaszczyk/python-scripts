"""Queries Google for each line in a file."""

import webbrowser
import urllib.parse
import time


def read_from_file(path):
    """
    Reads the content of a file line by line.

    Args:
        path (str): The path to the file.

    Returns:
        list: A list of strings where each string is a line from the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        Exception: If there is an error reading the file.
    """
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"File not found: {path}")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def google_it(path):
    """
    Opens a new tab in the default web browser for each line in the file.

    Args:
        path (str): The path to the file.

    Note:
        After every 5 queries, the function waits for the user to press Enter before continuing.
        This is to prevent the browser from blocking the script due to too many requests.
        Please, do not abuse this script.
    """
    for i, entry in enumerate(read_from_file(path)):
        google_search(entry)
        if (i + 1) % 5 == 0:
            print(f"Total queries: {i + 1}. Press Enter to perform 5 more queries...")
            input()
        else:
            time.sleep(1)


def google_search(query):
    """
    Opens a new tab in the default web browser with a Google search for the query.

    Args:
        query (str): The search query.
    """
    query_encoded = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={query_encoded}"
    webbrowser.open_new_tab(url)


if __name__ == "__main__":
    """
    Parses command line arguments and starts the google_it function with the provided input file.
    """

    import argparse
    parser = argparse.ArgumentParser(description="Google entries from file.")
    parser.add_argument("-i", "--input", type=str, help="Path to the file with the entries.", required=True)
    args = parser.parse_args()

    google_it(args.input)
