FROM python:3.9

WORKDIR /app

COPY seeder.py .
COPY data_generator.py .
COPY main.py .

# Generate and seed data
RUN pip install Faker psycopg2-binary

CMD ["python", "main.py"]
