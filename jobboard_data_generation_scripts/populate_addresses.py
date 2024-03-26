from faker import Faker
from faker.providers import address, company, currency, date_time, file, job, lorem
from sql_metadata import Parser
import sys

# INSERT INTO address (street, city, postal_code, country, company_id)
# VALUES (
#         '1600 Amphitheatre Parkway',
#         'Mountain View',
#         '94043',
#         'USA',
#         2
#     );

def generate_street_names(amount):
    fake = Faker()
    fake.add_provider(address)
    street_names = []
    for _ in range(amount):
        street_names.append(fake.street_name())
    return street_names

def generate_cities(amount):
    fake = Faker()
    fake.add_provider(address)
    cities = []
    for _ in range(amount):
        cities.append(fake.city())
    return cities

def generate_postal_codes(amount):
    fake = Faker()
    fake.add_provider(address)
    postal_codes = []
    for _ in range(amount):
        postal_codes.append(fake.postcode())
    return postal_codes

def generate_countries(amount):
    fake = Faker()
    fake.add_provider(address)
    countries = []
    for _ in range(amount):
        countries.append(fake.country())
    return countries

# Since we cannot assign an address to a company that does not exist,
# make sure to provide valid range for existing company id values (the amount of companies generated previously)
def generate_company_id(number_of_companies):
    fake = Faker()
    company_ids = []
    for _ in range(number_of_companies):
        company_ids.append(fake.random_int(min=1, max=number_of_companies))
    return company_ids

# TODO - Refactor this function
def assemble_queries(street_names, cities, postal_codes, countries, company_ids):
    queries = []
    for i in range(len(company_ids)):
        query = f"INSERT INTO address (street, city, postal_code, country, company_id) VALUES ('{street_names[i]}', '{cities[i]}', '{postal_codes[i]}', '{countries[i]}', {company_ids[i]});"
        queries.append(query)
    return queries

def write_queries_to_file(queries):
    with open('populate_addresses.sql', 'w') as file:
        for query in queries:
            file.write(query + '\n')

def main():
    if len(sys.argv) < 3:
        print("Amount of addresses to generate is required as an argument. Example: python populate_addresses.py 10 20")
        print("Amount of companies generated previously is required as an argument. Example: python populate_addresses.py 10 10")
        print("Make sure to generate companies first before generating addresses. The company id must exist in the database.")
        print("Otherwise, the foreign key constraint will fail.")
        return
    
    amount = int(sys.argv[1])
    number_of_companies = int(sys.argv[2])
    street_names = generate_street_names(amount)
    cities = generate_cities(amount)
    postal_codes = generate_postal_codes(amount)
    countries = generate_countries(amount)
    company_ids = generate_company_id(number_of_companies)
    queries = assemble_queries(street_names, cities, postal_codes, countries, company_ids)
    write_queries_to_file(queries)

if __name__ == "__main__":
    main()