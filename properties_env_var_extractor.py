"""Module to extract environment variables from a properties file."""
import argparse


def open_file(file_path):
    """
    Opens a file and returns its content as a list of lines.

    Args:
        file_path (str): The path to the file to be opened.

    Returns:
        list: A list of lines from the file.

    """
    lines = []

    with open(file_path, "r", encoding="UTF-8") as file:
        lines = file.readlines()

    return lines


def parse_data(data):
    """
    Parses the properties file and extracts environment variables.

    Args:
        data (list): List of lines from the properties file.

    Returns:
        dict: Dictionary containing properties and their values.

    """
    properties_dict = {}

    for line in data:
        if line.startswith("#") or line.startswith("\n"):
            continue
        # Check if the line contains a = sign
        if "=" not in line or "${" not in line:
            continue
        else:
            key, value = line.split("=")
            key = key.strip()
            value = value.strip()

        properties_dict[key] = value

    return properties_dict


def extract_environment_variables(data):
    """
    Extracts environment variables from the properties data.

    Args:
        data (dict): Dictionary containing properties and their values.

    Returns:
        dict: Dictionary containing environment variables and their default values.

    """
    environment_variables = {}

    for key, value in data.items():
        if ":" in value:
            parts = value.split(":", 1)
            env_var = parts[0].replace("${", "").replace("}", "")
            default_value = parts[1].replace("}", "") if len(parts) > 1 else None
            environment_variables[env_var] = default_value

    return environment_variables


def write_to_markdown_table(properties_dict, env_variables_dict):
    """
    Writes the extracted data to a markdown table.

    Args:
        properties (dict): Dictionary containing properties and their values.
        env_variables (dict): Dictionary containing environment variables and their default values.

    """
    with open("data.md", "w", encoding="UTF-8") as file:
        file.write("| **Environment variable** | **Default value** | **Corresponding property name** | **Description** |\n")
        file.write("| --- | --- | --- | --- |\n")

        for env_var, default_value in env_variables_dict.items():
            for key, value in properties_dict.items():
                if env_var in value:
                    file.write(f"| `{env_var}` | {default_value} | `{key}` |  |\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Extract environment variables from properties file"
    )
    parser.add_argument(
        "--path", "-p", type=str, help="Path to the properties file"
    )

    args = parser.parse_args()

    if args is None:
        parser.error("No arguments or path provided")
    else:
        data_from_file = open_file(args.path)
        properties = parse_data(data_from_file)
        env_variables = extract_environment_variables(properties)
        write_to_markdown_table(properties, env_variables)
        print("Successfully written to file")
