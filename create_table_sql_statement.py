import argparse


def write_to_file(filename, text, append=False):

    if append:
        with open(filename, "a") as f:
            # Since text is a list, join it into a string
            f.write("\n".join(text))
    else:
        # If the file does not exist, create it
        with open(filename, "w") as f:
            f.write("\n".join(text))


def create_table(name, columns, types):

    text = []

    if len(columns) != len(types):
        raise ValueError("There must be the same number of columns and types")

    text.append(f"CREATE TABLE {name} ")
    text.append("(")

    # If there is only one column, do not add a comma
    # Otherwise, add a comma after each but the last column

    if len(columns) == 1:
        text.append(f"{columns[0]}  {types[0]}")
    else:
        for i in range(len(columns)):
            if i != len(columns) - 1:
                text.append(f"{columns[i]}  {types[i]},")
            else:
                text.append(f"{columns[i]}  {types[i]}")
    text.append(");")

    return text


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate SQL statement for creating a table")
    parser.add_argument(
        "--name", "-n", help="name of the table", action="store")
    parser.add_argument(
        "--columns", "-c", nargs="+", help="columns of the table", action="store")
    parser.add_argument(
        "--types", "-t", nargs="+", help="types of the columns", action="store")
    parser.add_argument(
        "--append", "-a", help="append to the file", action="store_true")
    parser.add_argument(
        "--output", "-o", help="output file", action="store")

    args = parser.parse_args()

    if args.columns is None or args.types is None or args.name is None or args.output is None:
        parser.error(
            "You must supply a table name, at least one column name, its corresponding type and an output file")

    columns = args.columns
    types = args.types

    text = create_table(args.name, columns, types)

    if args.append:
        write_to_file(args.output, text, append=True)
    else:
        write_to_file(args.output, text)
