<!-- ABOUT  -->
## About 

This is a collection of python scripts that I have written for various purposes. For shell scripts, [check out this repository](https://github.com/kapiaszczyk/scripts).

<!-- GETTING STARTED -->
## Getting Started

To run these scripts, you will need to have python installed on your machine. You can download python from the official website [here](https://www.python.org/downloads/).

<!-- Details-->
## Detailed instructions

### [parse_md_to_anki_csv.py](https://github.com/kapiaszczyk/python-scripts/blob/main/parse_md_to_anki_csv.py)

This script parses markdown notes to a CSV file that can be imported into Anki. The script is designed to work with notes that are formatted in a specific way.
You can find more details in the [DOCS.md](https://github.com/kapiaszczyk/python-scripts/blob/main/anki/DOCS.md) file.

### [extract_openapi_paths.py](https://github.com/kapiaszczyk/python-scripts/blob/main/extract_openapi_paths.py)

This script extracts API paths from openAPI v3 documentation. It works with both YAML and JSON files and can output the paths to a simple markdown table.

Usage:
```
python extract_openapi_paths.py -p <path_to_openapi_documentation> -t <True/False> -y <True/False>
```

### [properties_env_var_extractor.py](https://github.com/kapiaszczyk/python-scripts/blob/main/properties_env_var_extractor.py)

This script extracts environment variables for `application.properties` file of Spring application and generates a markdown table with variable name, default value and corresponding property. It does not support multiple variables in one property (eg. `spring.datasource.url=${URL:jdbc:postgresql://localhost:5432}/${NAME:name}`) and leaves the description column empty.

Usage:
```
python properties_env_var_extractor.py [-h] [--path PATH]
```

### [jobboard_data_generation_scripts](https://github.com/kapiaszczyk/python-scripts/tree/main/jobboard_data_generation_scripts)

Scripts that generate test data for one of my personal projects with help of Faker library.

### [create_table_sql_statement.py](https://github.com/kapiaszczyk/python-scripts/blob/main/create_table_sql_statement.py)

Simple script that generates a SQL create table statement. Perfect when for creating table fast. Doesn't support constraints etc.

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE.txt` for more information.
