from faker import Faker
import sys

# SQL schema for job_offer table
# -- CREATE TYPE salary_type_enum AS ENUM ('hourly', 'monthly', 'annual', 'other');
# -- CREATE TYPE operating_mode_enum AS ENUM ('remote', 'hybrid', 'onsite');

# -- CREATE TABLE job_offer (
# --     id SERIAL PRIMARY KEY,
# --     name VARCHAR(255) NOT NULL,
# --     short_description VARCHAR(255) NOT NULL,
# --     description TEXT NOT NULL,
# --     contract_type VARCHAR(255) NOT NULL,
# --     salary INT NOT NULL,
# --     salary_currency VARCHAR(255) NOT NULL,
# --     salary_type salary_type_enum NOT NULL,
# --     experience VARCHAR(255) NOT NULL,
# --     operating_mode operating_mode_enum NOT NULL,
# --     company_id INT,
# --     address_id INT,
# --     FOREIGN KEY (company_id) REFERENCES company(id),
# --     FOREIGN KEY (address_id) REFERENCES address(id)
# -- );


contract_type = ["full-time", "b2b", "part-time",
                 "internship", "contract", "other"]

salary_type = ["hourly", "monthly", "annual", "other"]

experience = ["intern", "junior", "regular", "mid", "senior", "architect"]

job_names_examples = ["Software Engineer", "Data Scientist", "Product Manager", "QA Engineer", "DevOps Engineer", "Frontend Developer", "Backend Developer",
                      "Fullstack Developer", "Mobile Developer", "UX/UI Designer", "Scrum Master", "Project Manager", "Business Analyst", "Sales Manager",
                      "HR Specialist", "Recruiter", "Office Manager", "Customer Support Specialist", "Marketing Specialist", "Content Creator",
                      "Graphic Designer", "System Administrator", "Network Administrator", "Cloud Engineer", "Security Specialist", "Database Administrator",
                      "Data Analyst", "Data Engineer", "Machine Learning Engineer", "AI Specialist", "Blockchain Developer", "Game Developer", "Embedded Developer"]

operating_modes = ["remote", "hybrid", "onsite"]

fake = Faker()


def get_job_name():
    return fake.random_element(job_names_examples)


def get_short_desc():
    return fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)


def generate_description():
    return fake.text()


def generate_contract_type():
    return fake.random_element(contract_type)


def generate_salary():
    return fake.random_int(min=100, max=300_000)


def generate_currency():
    return fake.currency_code()


def generate_salary_type():
    return fake.random_element(salary_type)


def get_experience(amount):
    return fake.random_element(experience)


def get_operating_mode():
    return fake.random_element(operating_modes)


def get_boolean():
    return fake.boolean(chance_of_getting_true=50)


def get_company_id(number_of_companies):
    return fake.random_int(min=1, max=number_of_companies)


def assemble_queries(amount, number_of_companies):
    queries = []
    for i in range(amount):
        # Since the addresses are generated sequentially, assign the same address_id as company_id
        company_address_id = get_company_id(number_of_companies)
        query = f"INSERT INTO job_offer (name, short_description, description, contract_type, salary, salary_currency, salary_type, experience, operating_mode, company_id, address_id) VALUES ('{get_job_name()}', '{get_short_desc()}', '{
            generate_description()}', '{generate_contract_type()}', {generate_salary()}, '{generate_currency()}', '{generate_salary_type()}', '{get_experience(amount)}', '{get_operating_mode()}', {company_address_id}, {company_address_id});"
        queries.append(query)
    return queries


def write_to_file(queries):
    with open("populate_job_offers.sql", "w") as file:
        for query in queries:
            file.write(query + "\n")


def main():
    if len(sys.argv) != 3:
        print("Usage: python populate_job_offers.py <amount_of_job_offers> <number_of_companies>")
        print("The amount of job offers should be greater than the number of companies.")
        exit(1)

    amount_of_job_offers = int(sys.argv[1])
    number_of_companies = int(sys.argv[2])

    queries = assemble_queries(amount_of_job_offers, number_of_companies)
    write_to_file(queries)


if __name__ == "__main__":
    main()
