from faker import Faker
import sys

fake = Faker()

degree_of_knowledge_examples = ["no knowledge required", "beginner", "intermediate", "advanced", "expert"]

def generate_knowledge_levels(amount):
    return [fake.random_element(degree_of_knowledge_examples) for _ in range(amount)]

def generate_job_offer_technologies(range_of_job_offers, range_of_technologies):
    queries = []
    for job_offer_id in range(range_of_job_offers):
        amount_of_technologies = fake.random_int(min=1, max=5)
        used_technologies = set()  # Keep track of used technology ids for this job offer
        for _ in range(amount_of_technologies):
            technology_id = fake.random_int(min=1, max=range_of_technologies)
            while technology_id in used_technologies:
                technology_id = fake.random_int(min=1, max=range_of_technologies)  # Generate a new id until it's unique
            used_technologies.add(technology_id)
            knowledge_level = fake.random_element(degree_of_knowledge_examples)  # Assuming you have a list of degree_of_knowledge_examples
            queries.append(
                f"INSERT INTO job_offer_technology (job_offer_id, technology_id, degree_of_knowledge) "
                f"VALUES ({job_offer_id + 1}, {technology_id}, '{knowledge_level}');"
            )
    return queries

def write_to_file(queries):
    with open("populate_job_offer_technologies.sql", "w") as file:
        for query in queries:
            file.write(str(query) + "\n")

def main():
    range_of_job_offers = int(sys.argv[1])
    range_of_technologies = int(sys.argv[2])

    queries = generate_job_offer_technologies(range_of_job_offers, range_of_technologies)
    write_to_file(queries)

if __name__ == "__main__":
    main()
