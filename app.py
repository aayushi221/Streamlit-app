import streamlit as st
import snowflake.connector # type: ignore

# Establishing connection to Snowflake
def create_snowflake_connection():
    conn = snowflake.connector.connect(
        user='GROUP3',
        password='Stats_project@1234',
        account='ut67848.ca-central-1',
        warehouse='COMPUTE_WH',
        database='INSTAGRAM',
        schema='PUBLIC'
    )
    return conn

# Display Data from Snowflake
def display_data_from_snowflake():
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM test")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

# Streamlit App
st.title("Snowflake Data Viewer")
data = display_data_from_snowflake()
st.write("Data from Snowflake:", data)
