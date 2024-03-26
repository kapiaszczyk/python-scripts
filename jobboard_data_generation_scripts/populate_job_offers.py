from faker import Faker
from faker.providers import address, company, currency, date_time, file, job, lorem
from sql_metadata import Parser
import sys


# CREATE TYPE salary_type_enum AS ENUM ('hourly', 'monthly', 'annual', 'other');

# INSERT INTO job_offer (name, short_description, description, contract_type, salary, salary_currency, salary_type, seniority_level, is_remote, is_hybrid, company_id)
# VALUES (
#         'Software Engineer',
#         'Develop software',
#         'Develop software for the company',
#         'Full-time',
#         100000,
#         'USD',
#         'annual',
#         'Junior',
#         false,
#         false,
#         1
#     );

contract_type = ["full-time", "b2b", "part-time", "internship", "contract", "other"]

salary_type = ["hourly", "monthly", "annual", "other"]

seniority_level = ["intern", "junior", "regular", "mid", "senior", "architect"]

job_names_examples = ["Software Engineer", "Data Scientist", "Product Manager", "QA Engineer", "DevOps Engineer", "Frontend Developer", "Backend Developer", 
             "Fullstack Developer", "Mobile Developer", "UX/UI Designer", "Scrum Master", "Project Manager", "Business Analyst", "Sales Manager", "HR Specialist", "Recruiter", 
             "Office Manager", "Customer Support Specialist", "Marketing Specialist", "Content Creator", "Graphic Designer", "System Administrator", "Network Administrator",
             "Cloud Engineer", "Security Specialist", "Database Administrator", "Data Analyst", "Data Engineer", "Machine Learning Engineer", "AI Specialist", "Blockchain Developer",
                "Game Developer", "Embedded Developer"]

def generate_job_names(amount):
    fake = Faker()
    fake.add_provider(job)
    job_names = []
    for _ in range(amount):
        job_names.append(fake.random_element(job_names_examples))
    return job_names


def generate_short_descriptions(amount):
    short_descriptions = []
    fake = Faker()
    for _ in range(amount):
        short_descriptions.append(fake.word())



    return short_descriptions

def generate_description(amount):
    descriptions = []
    fake = Faker()
    for _ in range(amount):
        descriptions.append(fake.paragraph(nb_sentences=1))


    return descriptions

def generate_contract_type(amount):
    contract_types = []
    fake = Faker()
    for _ in range(amount):
        contract_types.append(fake.random_element(contract_type))


    return contract_types


def generate_salary(amount):
    salaries = []
    fake = Faker()
    for _ in range(amount):
        salaries.append(fake.random_int(min=100, max=300_000))


    return salaries

def generate_currency(amount):
    currencies = []
    fake = Faker()
    for _ in range(amount):
        currencies.append(fake.currency_code())
    

    return currencies

def generate_salary_type(amount):
    salary_types = []
    fake = Faker()
    for _ in range(amount):
        salary_types.append(fake.random_element(salary_type))


    return salary_types

def generate_seniority_level(amount):
    seniority_levels = []
    fake = Faker()
    for _ in range(amount):
        seniority_levels.append(fake.random_element(seniority_level))


    return seniority_levels

def generate_random_boolean():
    faker = Faker()

    value = faker.boolean(chance_of_getting_true=50)


    return value

def generate_random_company_ids(amount, company_range):
    company_ids = []
    fake = Faker()
    for _ in range(amount):
        company_ids.append(fake.random_int(min=1, max=company_range))


    return company_ids

def assemble_queries(job_names, short_descriptions, descriptions, contract_types, salaries, currencies, salary_types, seniority_levels, company_ids):
    queries = []
    for i in range(len(job_names)):
        query = f"INSERT INTO job_offer (name, short_description, description, contract_type, salary, salary_currency, salary_type, seniority_level, is_remote, is_hybrid, company_id) VALUES ('{job_names[i]}', '{short_descriptions[i]}', '{descriptions[i]}', '{contract_types[i]}', {salaries[i]}, '{currencies[i]}', '{salary_types[i]}', '{seniority_levels[i]}', {generate_random_boolean()}, {generate_random_boolean()}, {company_ids[i]});"
        queries.append(query)
    return queries

def write_to_file(queries):
    with open("populate_job_offers.sql", "w") as file:
        for query in queries:
            file.write(query + "\n")

def main():
    amount = int(sys.argv[1])
    number_of_companies = int(sys.argv[2])
    job_names = generate_job_names(amount)
    short_descriptions = generate_short_descriptions(amount)
    descriptions = generate_description(amount)
    contract_types = generate_contract_type(amount)
    salaries = generate_salary(amount)
    currencies = generate_currency(amount)
    salary_types = generate_salary_type(amount)
    seniority_levels = generate_seniority_level(amount)
    company_ids = generate_random_company_ids(amount, number_of_companies)
    queries = assemble_queries(job_names, short_descriptions, descriptions, contract_types, salaries, currencies, salary_types, seniority_levels, company_ids)
    write_to_file(queries)

if __name__ == "__main__":
    main()