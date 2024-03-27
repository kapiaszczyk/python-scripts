from faker import Faker
from faker.providers import address
import sys
from random import sample

fake = Faker()


def generate_street_names(amount):
    fake.add_provider(address)
    street_names = [fake.street_name() for _ in range(amount)]
    return street_names


def generate_cities(amount):
    fake.add_provider(address)
    cities = [fake.city() for _ in range(amount)]
    return cities


def generate_postal_codes(amount):
    fake.add_provider(address)
    postal_codes = [fake.postcode() for _ in range(amount)]
    return postal_codes


def generate_countries(amount):
    fake.add_provider(address)
    countries = [fake.country() for _ in range(amount)]
    return countries


def generate_company_id(amount, number_of_companies):
    company_ids = []

    # First fill with all company ids
    for _ in range(1, number_of_companies + 1):
        company_ids.append(_)

    # For amount of addresses left, add random company ids
    for _ in range(amount - number_of_companies):
        company_ids.append(sample(range(1, number_of_companies + 1), 1)[0])

    return company_ids


def assemble_queries(street_names, cities, postal_codes, countries, company_ids):
    queries = []
    for i in range(len(company_ids)):
        query = f"INSERT INTO address (street, city, postal_code, country, company_id) VALUES ('{
            street_names[i]}', '{cities[i]}', '{postal_codes[i]}', '{countries[i]}', {company_ids[i]});"
        queries.append(query)
    return queries


def write_queries_to_file(queries):
    with open('populate_addresses.sql', 'w') as file:
        for query in queries:
            file.write(query + '\n')


def main():
    if len(sys.argv) < 3:
        print("Usage: python populate_addresses.py <amount_of_addresses> <number_of_companies>")
        print("Amount of addresses should be equal or greater than the number of companies. More addresses mean more companies with multiple locations.")
        return

    amount = int(sys.argv[1])
    number_of_companies = int(sys.argv[2])

    street_names = generate_street_names(amount)
    cities = generate_cities(amount)
    postal_codes = generate_postal_codes(amount)
    countries = generate_countries(amount)
    company_ids = generate_company_id(amount, number_of_companies)
    queries = assemble_queries(
        street_names, cities, postal_codes, countries, company_ids)
    write_queries_to_file(queries)


if __name__ == "__main__":
    main()
