from faker import Faker
from faker.providers import address, company, currency, date_time, file, job, lorem
from sql_metadata import Parser
import sys


# Example query to insert a new company into the database
# INSERT INTO company (name, description, website, email)
# VALUES (
#         'Apple',
#         'Apple Inc. is an American multinational technology company that specializes in consumer electronics, computer software, and online services.',
#         'https://www.apple.com',
#         'recruitment@apple.com'
#     );

def generate_company_names(amount):
    fake = Faker()
    fake.add_provider(company)
    company_names = []
    for _ in range(amount):
        company_names.append(fake.company())
    return company_names

def generate_company_descriptions(amount):
    fake = Faker()
    company_descriptions = []
    for _ in range(amount):
        company_descriptions.append(fake.paragraph(nb_sentences=1))
    return company_descriptions

def generate_company_websites(amount):
    fake = Faker()
    company_websites = []
    for _ in range(amount):
        company_websites.append(fake.url())
    return company_websites

def generate_company_emails(amount):
    fake = Faker()
    company_emails = []
    for _ in range(amount):
        company_emails.append(fake.email())
    return company_emails

def assemble_queries(company_names, company_descriptions, company_websites, company_emails):
    queries = []
    for i in range(len(company_names)):
        query = f"INSERT INTO company (name, description, website, email) VALUES ('{company_names[i]}', '{company_descriptions[i]}', '{company_websites[i]}', '{company_emails[i]}');"
        queries.append(query)
    return queries

def write_queries_to_file(queries):
    with open('populate_companies.sql', 'w') as file:
        for query in queries:
            file.write(query + '\n')

def main():
    if len(sys.argv) < 2:
        print("Amount of companies to generate is required as an argument. Example: python populate_companies.py 10")
        return

    amount = int(sys.argv[1])
    names = generate_company_names(amount)
    descriptions = generate_company_descriptions(amount)
    websites = generate_company_websites(amount)
    emails = generate_company_emails(amount)
    queries = assemble_queries(names, descriptions, websites, emails)
    write_queries_to_file(queries)

if __name__ == "__main__":
    main()