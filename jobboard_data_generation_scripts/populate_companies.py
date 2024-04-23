from faker import Faker
from faker.providers import company
import sys

fake = Faker()

def generate_company_names(amount):
    fake.add_provider(company)
    company_names = [fake.company() for _ in range(amount)]
    return company_names

def generate_company_descriptions(amount):
    company_descriptions = [fake.paragraph(nb_sentences=5) for _ in range(amount)]
    return company_descriptions

def generate_company_websites(amount):
    company_websites = [(f"https://{fake.word()}.{fake.random_element(elements=('com', 'net', 'org'))}") for _ in range(amount)]
    return company_websites

def generate_company_emails(amount):
    company_emails = [(f"{fake.word()}@{fake.word()}.com") for _ in range(amount)]
    return company_emails

def assemble_queries(company_names, company_descriptions, company_websites, company_emails):
    queries = [f"INSERT INTO company (name, description, website, email) VALUES ('{company_names[i]}', '{company_descriptions[i]}', '{company_websites[i]}', '{company_emails[i]}');" for i in range(len(company_names))]
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