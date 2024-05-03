import argparse
import json
import yaml


FILE_NAME_MD = "endpoints.md"
FILE_NAME_TXT = "endpoints.txt"


def read_documentation(path):
    """Reads OpenAPI documentation from a file

    Args:
        path (str): Path to the OpenAPI documentation file

    Returns:
        str: OpenAPI documentation content
    """
    with open(path, "r", encoding="UTF-8") as file:
        read_doc = file.read()
    return read_doc


def extract_endpoints_from_json(documentation_json):
    """Extracts endpoints from OpenAPI documentation in JSON format

    Args:
        documentation_json (str): OpenAPI documentation in JSON format

    Returns:
        list: List of extracted endpoints
    """
    documentation_json = json.loads(documentation_json)
    paths_json = documentation_json["paths"]
    paths_list = []
    for path in paths_json:
        paths_list.append(path)
    return paths_list


def extract_endpoints_from_yaml(documentation_yaml):
    """Extracts endpoints from OpenAPI documentation in YAML format

    Args:
        documentation_yaml (str): OpenAPI documentation in YAML format

    Returns:
        list: List of extracted endpoints
    """
    documentation_yaml = yaml.safe_load(documentation_yaml)
    paths_yaml = documentation_yaml["paths"]
    paths_list = []
    for path in paths_yaml:
        paths_list.append(path)
    return paths_list


def extract_endpoint_description(documentation_json):
    """Extracts endpoint description from OpenAPI documentation in JSON format

    Args:
        documentation_json (str): OpenAPI documentation in JSON format

    Returns:
        dict: Dictionary of endpoints and their descriptions
    """
    documentation_json = json.loads(documentation_json)
    paths_json = documentation_json["paths"]
    paths_dict = {}
    for path in paths_json:
        paths_dict[path] = paths_json[path]
    return paths_dict


def extract_endpoint_description_yaml(documentation_yaml):
    """Extracts endpoint description from OpenAPI documentation in YAML format

    Args:
        documentation_yaml (str): OpenAPI documentation in YAML format

    Returns:
        dict: Dictionary of endpoints and their descriptions
    """
    documentation_yaml = yaml.safe_load(documentation_yaml)
    paths_yaml = documentation_yaml["paths"]
    paths_dict = {}
    for path in paths_yaml:
        paths_dict[path] = paths_yaml[path]
    return paths_dict


def write_to_markdown_table(endpoint_dict):
    """Writes the extracted endpoints to a markdown table

    Args:
        endpoint_dict (dict): Dictionary containing endpoint paths and associated data
    """
    with open(FILE_NAME_MD, "w", encoding="UTF-8") as file:
        file.write("| **Endpoint** | **Method** | **Description** |\n")
        file.write("| --- | --- | --- |\n")
        for endpoint, methods in endpoint_dict.items():
            for method, data in methods.items():
                try:
                    summary = data['summary']
                except KeyError:
                    print(f"Error: Could not extract summary for endpoint: {endpoint}")
                    summary = "No summary available"
                file.write(f"| `{endpoint}` | *{method.upper()}* | {summary} |\n")


def write_to_file(endpoint_list):
    """Writes the extracted endpoints to a file
    
    Args:
        endpoint_list (list): List of extracted endpoints
    """
    with open(FILE_NAME_TXT, "w", encoding="UTF-8") as file:
        file.write(endpoint_list)


def success_message():
    """Prints a success message to the console after writing to file"""
    print("Successfully written to file")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Extract endpoints from OpenAPI documentation"
    )
    parser.add_argument(
        "--path", "-p", type=str, help="OpenAPI documentation file path", action="store"
    )
    parser.add_argument(
        "--table",
        "-t",
        type=bool,
        help="Print the extracted endpoints in a markdown table",
        action="store",
    )
    parser.add_argument(
        "--yaml",
        "-y",
        type=bool,
        help="Read OpenAPI documentation in YAML format",
        action="store",
    )

    args = parser.parse_args()

    if args is None:
        parser.error("No arguments or path provided")

    if args.path:
        documentation = read_documentation(args.path)
        if args.yaml:
            endpoints = extract_endpoints_from_yaml(documentation)
            if args.table:
                descriptions = extract_endpoint_description_yaml(documentation)
                write_to_markdown_table(descriptions)
            else:
                write_to_file(endpoints)
        else:
            endpoints = extract_endpoints_from_json(documentation)
            if args.table:
                descriptions = extract_endpoint_description(documentation)
                write_to_markdown_table(descriptions)
            else:
                write_to_file(endpoints)
        success_message()
    else:
        parser.error("No path provided")
