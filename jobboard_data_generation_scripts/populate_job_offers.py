from faker import Faker
import sys

contract_type = ["full-time", "b2b", "part-time",
                 "internship", "contract", "other"]

salary_type = ["hourly", "monthly", "annual", "other"]

seniority_level = ["intern", "junior", "regular", "mid", "senior", "architect"]

job_names_examples = ["Software Engineer", "Data Scientist", "Product Manager", "QA Engineer", "DevOps Engineer", "Frontend Developer", "Backend Developer",
                      "Fullstack Developer", "Mobile Developer", "UX/UI Designer", "Scrum Master", "Project Manager", "Business Analyst", "Sales Manager",
                      "HR Specialist", "Recruiter", "Office Manager", "Customer Support Specialist", "Marketing Specialist", "Content Creator",
                      "Graphic Designer", "System Administrator", "Network Administrator", "Cloud Engineer", "Security Specialist", "Database Administrator",
                      "Data Analyst", "Data Engineer", "Machine Learning Engineer", "AI Specialist", "Blockchain Developer", "Game Developer", "Embedded Developer"]

fake = Faker()


def get_job_name():
    return fake.random_element(job_names_examples)


def get_short_desc():
    return fake.word()


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


def get_seniority_level(amount):
    return fake.random_element(seniority_level)


def get_boolean():
    return fake.boolean(chance_of_getting_true=50)


def get_company_id(number_of_companies):
    return fake.random_int(min=1, max=number_of_companies)


def assemble_queries(amount, number_of_companies):
    queries = []
    for i in range(amount):
        query = f"INSERT INTO job_offer (name, short_description, description, contract_type, salary, salary_currency, salary_type, seniority_level, is_remote, is_hybrid, company_id) VALUES ('{get_job_name()}', '{get_short_desc()}', '{
            generate_description()}', '{generate_contract_type()}', {generate_salary()}, '{generate_currency()}', '{generate_salary_type()}', '{get_seniority_level()}', {get_boolean()}, {get_boolean()}, {get_company_id(number_of_companies)});"
        queries.append(query)
    return queries


def write_to_file(queries):
    with open("populate_job_offers.sql", "w") as file:
        for query in queries:
            file.write(query + "\n")


def main():
    amount_of_job_offers = int(sys.argv[1])
    number_of_companies = int(sys.argv[2])

    if len(sys.argv) < 3:
        print("Usage: python populate_job_offers.py <amount_of_job_offers> <number_of_companies>")
        print("The amount of job offers should be greater than the number of companies.")
        exit(1)

    queries = assemble_queries(amount_of_job_offers, number_of_companies)
    write_to_file(queries)


if __name__ == "__main__":
    main()
