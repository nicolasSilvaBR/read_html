import streamlit as st
import pandas as pd
from functions.database_connection import mydb
from functions.secrets_config import get_secrets_config

def main():
    st.title("Database Query")

    # Connect to the database
    engine = mydb()
    if engine is None:
        st.error("Database connection could not be established.")
        return

    db_config = get_secrets_config()
    if db_config is None:
        st.error("Failed to load database configuration.")
        return

    sql_query = """  
        SELECT * FROM dbo.HTML_Content
    """
    
    try:
        # Read the SQL query into a DataFrame
        df = pd.read_sql_query(sql_query, engine)

        # Check if there is data and display it
        if not df.empty:
            st.success("Query executed successfully!")
            st.dataframe(df)  # Display the table in Streamlit
        else:
            st.warning("No data found in the 'test' table.")
    except Exception as e:
        st.error(f"Error executing query: {e}")

# Run Streamlit
if __name__ == "__main__":
    main()
