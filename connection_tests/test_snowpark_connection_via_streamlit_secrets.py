
# Test connection to Snowpark leveraging Streamlit secrets

## Import required function
from interworks_snowpark.snowpark_session_builder import build_snowpark_session_via_streamlit_secrets as build_snowpark_session

## Generate Snowpark session
snowpark_session = build_snowpark_session()

## Simple commands to test the connection by listing the databases in the environment
df_test = snowpark_session.sql('SHOW DATABASES')
df_test.show()
