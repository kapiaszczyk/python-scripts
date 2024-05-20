import argparse
import logging
import flatdict
import yaml


def convert(input_path):
    """Converts and saves the converted file."""

    if input_path.lower().endswith('.yaml'):
        content = convert_to_properties(input_path)
        output_path = input_path.lower().replace(".yaml", ".properties")
        save(content, output_path)
    elif input_path.lower().endswith('.properties'):
        content = convert_to_yaml(input_path)
        output_path = input_path.lower().replace(".properties", ".yaml")
        save(content, output_path)
    else:
        raise ValueError("File is neither a properties or YAML format")


def convert_to_properties(file):
    """Converts a YAML file to properties file

        The function flattens the YAML content into a dictionary,
        then iterates over it, creating a list.
        The list is then joined into a single string.
        Colons in the keys are replaced with dots.

    """

    content = yaml.load(read(file), Loader=yaml.FullLoader)

    flattened = flatdict.FlatDict(content)

    result = []

    for key, value in flattened.items():
        result.append(f"{key}={value}")

    result = "\n".join(result)

    result = result.replace(":", ".")

    return result


def convert_to_yaml(file):
    """Converts a properties file to a YAML file.

        The function creates a nested dictionaries based on key parts.
        For each line, points the current level to the root of the dictionary
        and loops over the key parts, skipping the last part.
        Checks if given part exists at the current level.
        If it does not, creates a new dictionary at that part.
        If it does, moves the current level to that part.
        Finally, assigns the value to the last part of the key.

        Empty or commented out lines are skipped 
        and the output is parsed to YAML format.
    
    """

    content = read(file)

    result = {}

    for line in content.splitlines():
        line = line.strip()

        if not line or line.startswith('#'):
            continue

        key, value = line.split('=')
        key_parts = key.strip().split('.')

        current_dictionary_level = result

        for part in key_parts[:-1]:
            if part not in current_dictionary_level:
                current_dictionary_level[part] = {}
            current_dictionary_level = current_dictionary_level[part]
        current_dictionary_level[key_parts[-1]] = value.strip()

    return yaml.dump(result, default_flow_style=False)


def read(path):
    """Reads the file content and returns it"""

    try:
        with open(path, 'r', encoding="UTF-8") as file:
            return file.read()
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
    except Exception as e:
        logger.error(f"An error occurred while reading file: {e}")
        exit(1)


def save(content, path):
    """Saves the contents to a file."""

    try:
        with open(path, 'w', encoding="UTF-8") as file:
            file.write(content)
    except Exception as e:
        logger.error(f"An error occurred while saving file: {e}")


def setup_logging():
    """Setups logging."""
    logging.basicConfig(level="INFO", format="%(levelname)s - %(message)s")
    return logging.getLogger(__name__)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert properties to YAML and vice versa")

    parser.add_argument("--input", "-i", help="Path to the input file", required=True)

    logger = setup_logging()

    args = parser.parse_args()

    convert(args.input)
