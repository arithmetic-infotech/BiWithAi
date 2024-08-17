from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd
import time

class DatabaseConnector:
    def __init__(self):
        pass

    @staticmethod
    def execute_query(driver, username, password, host, port, database, query):
        try:
            # Create the connection string
            connection_string = f"{driver}://{username}:{password}@{host}:{port}/{database}"

            # Create the engine
            engine = create_engine(connection_string)

            # Measure the time before executing the query
            start_time = time.time()

            # Execute the query
            with engine.connect() as connection:
                result = pd.read_sql_query(text(query), connection)

            # Measure the time after executing the query
            end_time = time.time()
            execution_time = end_time - start_time

            # Print the result and the execution time
            print(f"Query executed in {execution_time:.4f} seconds")
            print("Result:", result)

            return result

        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            return None