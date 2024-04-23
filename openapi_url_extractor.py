import argparse
import json
import yaml

FILE_NAME_MD = "endpoints.md"
FILE_NAME_TXT = "endpoints.txt"
USAGE = "Usage: python extract_endpoints.py -p <path_to_openapi_documentation> -t <True/False> -y <True/False>"


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


def write_to_markdown_table(endpoint_list):
    """Writes the extracted endpoints to a markdown table

    Args:
        endpoint_list (list): List of extracted endpoints
    """
    with open(FILE_NAME_MD, "w", encoding="UTF-8") as file:
        file.write("| **Endpoint** | **Description** |\n")
        file.write("| --- | --- |\n")
        for endpoint in endpoint_list:
            file.write(f"| `{endpoint}` |  |\n")


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

    if args is None or args.path is None:
        parser.error(USAGE)

    if args.yaml and args.path and not args.table:
        documentation = read_documentation(args.path)
        endpoints = extract_endpoints_from_yaml(documentation)
        write_to_file(endpoints)
        success_message()
    elif args.yaml and args.table and args.path:
        documentation = read_documentation(args.path)
        endpoints = extract_endpoints_from_yaml(documentation)
        write_to_markdown_table(endpoints)
        success_message()
    elif args.table and args.path:
        documentation = read_documentation(args.path)
        endpoints = extract_endpoints_from_json(documentation)
        write_to_markdown_table(endpoints)
        success_message()
    elif args.path and not args.table:
        documentation = read_documentation(args.path)
        endpoints = extract_endpoints_from_json(documentation)
        write_to_file(endpoints)
        success_message()
    else:
        parser.error(USAGE)
