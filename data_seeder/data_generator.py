"""
This script is used to generate data provided schema
"""

import os
import json
import random

from faker import Faker


def generate_fake_persons(faker, count):
    """
    this function generates fake persons
    """

    data = []
    for _ in range(count):
        id = "default"
        cognito_id = faker.uuid4()[:50]  # Limit to 50 characters
        first_name = faker.first_name()
        last_name = faker.last_name()
        birthdate = faker.date_of_birth(minimum_age=18, maximum_age=90)
        email = faker.email()
        phone_number = faker.phone_number()[:random.choice([12, 14, 16, 18, 20])]
        system_role = random.choice(['Admin', 'User'])
        created_at = faker.past_datetime(start_date="-30d", tzinfo=None)
        updated_at = faker.past_datetime(start_date=created_at, tzinfo=None)
        consents = faker.paragraph(nb_sentences=3)
        is_active = faker.boolean()

        data.append(
            [
                id,
                cognito_id,
                first_name,
                last_name,
                str(birthdate),
                email,
                phone_number,
                system_role,
                str(created_at),
                str(updated_at),
                consents,
                is_active
            ]
        )

    return data


def generate_fake_companies(faker, count):
    """
    this function generates fake persons
    """

    data = []
    for _ in range(count):
        id = "default"
        address = faker.address()
        name = faker.company()
        country = faker.country()[:50]
        id_number = faker.random_number(digits=8)
        vat_number = faker.random_number(digits=10)
        industry = faker.job()[:50]
        detailed_activity = faker.text(max_nb_chars=200)
        company_site = faker.url()
        size = random.choice(['Small', 'Medium', 'Large'])
        bank_account_country = faker.country()[:50]
        created_at = faker.past_datetime(start_date="-30d", tzinfo=None)
        updated_at = faker.past_datetime(start_date=created_at, tzinfo=None)
        is_active = faker.boolean()

        data.append(
            [
                id,
                address,
                name,
                country,
                id_number,
                vat_number,
                industry,
                detailed_activity,
                company_site,
                size,
                bank_account_country,
                str(created_at),
                str(updated_at),
                is_active
            ]
        )

    return data


if __name__ == "__main__":
    faker_obj = Faker()
    person_data_path = "./fake_person_data.json"
    company_data_path = "./fake_company_data.json"

    if not os.path.exists(person_data_path):
        person_data = generate_fake_persons(faker_obj, 5000)
        with open(person_data_path, 'w') as f:
            json.dump(person_data, f, indent=4)
        print("Person data are generated and saved")

    if not os.path.exists(company_data_path):
        company_data = generate_fake_companies(faker_obj, 5000)
        with open(company_data_path, 'w') as f:
            json.dump(company_data, f, indent=4)
        print("Company data are generated and saved")
