"""
This script is responsible for inserting data to postgresql
"""

import time
import json
import psycopg2


def connect_to_postgres(db_credentials):
    """
    connect to postgresql database
    """
    try:
        conn = psycopg2.connect(
            **db_credentials
        )

        return conn
    except psycopg2.OperationalError:
        print("Connection refused")
        time.sleep(5)
        return connect_to_postgres(db_credentials)


def load_json_data(json_file):
    """
    load data from json file
    """
    with open(json_file) as f:
        return json.load(f)


def prepare_insert_query(table_name, row):
    """
    prepare postgres insert query
    """
    args = []
    for val in row:
        if val is None:
            args.append("null")
        elif isinstance(val, bool):
            args.append(str(val).lower())
        elif val == "default":
            args.append("default")
        else:
            escaped_val = str(val).replace("\'", "")
            args.append(f"'{escaped_val}'")
    return f"INSERT INTO {table_name} VALUES ({', '.join(args)});"


def is_empty_table(cursor, table_name):
    """
    check if table is empty
    """
    cursor.execute(f"SELECT COUNT(*) FROM {table_name};")
    table_count = cursor.fetchone()[0]
    return table_count == 0


def insert_json_data(conn, data, table_name):
    """
    insert json data to postgres tables
    """
    cursor = conn.cursor()

    if is_empty_table(cursor, table_name):
        for row in data:
            cursor.execute(
                prepare_insert_query(table_name, row)
            )

        conn.commit()
        print(f"Inserted '{len(data)}' rows into '{table_name}' table")
    cursor.close()


def main():
    """
    main function
    """
    db_credentials = {
        "dbname": "mydb",
        "user": "myuser",
        "password": "mypass",
        "host": "postgresql",  # service name
        "port": 5432
    }

    person_data = load_json_data("./fake_person_data.json")
    company_data = load_json_data("./fake_company_data.json")
    connection = connect_to_postgres(db_credentials)

    insert_json_data(connection, person_data, "person")
    insert_json_data(connection, company_data, "company")

    connection.close()


if __name__ == "__main__":
    main()
