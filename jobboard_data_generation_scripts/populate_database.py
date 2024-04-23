import os
import sys


def main():

    if len(sys.argv) != 6:
        print("Usage: python populate_database.py <amount_of_technologies> <amount_of_companies> <amount_of_addresses> <amount_of_job_offers> <amount_of_technologies_job_offers>")
        return

    amount_of_technologies = int(sys.argv[1])
    amount_of_companies = int(sys.argv[2])
    amount_of_addresses = int(sys.argv[3])
    amount_of_job_offers = int(sys.argv[4])
    amount_of_technologies_job_offers = int(sys.argv[5])

    if amount_of_addresses < amount_of_companies:
        print("There must be more addresses than companies.")
        exit(1)

    if amount_of_technologies_job_offers < amount_of_job_offers:
        print("There must be more job_offer_technologies than job offers.")
        exit(1)

    # Create new directory to store the scripts
    if not os.path.exists("insert-statements"):
        os.makedirs("insert-statements")

    # Run the scripts
    print("Populating technologies...")
    exit_code = 0
    exit_code = exit_code or os.system(
        f"python populate_technologies.py {amount_of_technologies}")
    print("Populating companies...")
    exit_code = exit_code or os.system(
        f"python populate_companies.py {amount_of_companies}")
    print("Populating addresses...")
    exit_code = exit_code or os.system(f"python populate_addresses.py {amount_of_addresses} {amount_of_companies}")
    print("Populating job offers...")
    exit_code = exit_code or os.system(f"python populate_job_offers.py {amount_of_job_offers} {amount_of_companies}")
    print("Populating job offer technologies...")
    exit_code = exit_code or os.system(f"python populate_job_offer_technologies.py {amount_of_job_offers} {amount_of_technologies}")

    if exit_code != 0:
        print("An error occurred while running the scripts.")
        # Delete the files
        os.remove("populate_technologies.sql")
        os.remove("populate_companies.sql")
        os.remove("populate_addresses.sql")
        os.remove("populate_job_offers.sql")
        os.remove("populate_job_offer_technologies.sql")
    else:
        print("Database populated successfully.")

    # Rename the files
    # Since inserts are run after table creation, files should be renamed to start with a number
    os.rename("populate_technologies.sql",
              "insert-statements/01-populate_technologies.sql")
    os.rename("populate_companies.sql",
              "insert-statements/03-populate_companies.sql")
    os.rename("populate_addresses.sql",
              "insert-statements/05-populate_addresses.sql")
    os.rename("populate_job_offers.sql",
              "insert-statements/07-populate_job_offers.sql")
    os.rename("populate_job_offer_technologies.sql",
              "insert-statements/09-populate_job_offer_technologies.sql")


if __name__ == "__main__":
    main()
