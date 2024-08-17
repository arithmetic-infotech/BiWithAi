import streamlit as st

from com.aiwithbi.logging.Logger import Logger
from com.aiwithbi.prompt_processing import QueryGenerator
from com.aiwithbi.db.connetors import DatabaseConnector
from com.aiwithbi.exceptions import ModelInferenceError, DatabaseExecutionError
import com.aiwithbi.logging.Logger


# Initialize classes
query_generator = QueryGenerator.QueryGenerator("your-model-name")  # Replace with your actual model name
db_connector = DatabaseConnector.DatabaseConnector()  # Replace with your actual database URI

# Streamlit UI
st.title("AI-Powered Report Generator")

prompt = st.text_input("Enter your query in natural language:")

if st.button("Generate Report"):
    try:
        # Generate SQL Query
        query = query_generator.generate_sql_query(prompt)
        st.write(f"Generated SQL Query: {query}")

        # Execute SQL Query
        results = db_connector.execute_query(query)
        st.write("Query Results:")
        st.write(results)
    except ModelInferenceError as mie:
        st.error(f"Model error: {str(mie)}")
    except DatabaseExecutionError as dee:
        st.error(f"Database error: {str(dee)}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")


class RunBiWithAi:
    def __init__(self):
        Logger.setup_logging()
