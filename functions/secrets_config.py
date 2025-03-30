import os
import streamlit as st
import toml

def get_secrets_config():
    # Retrieve the configuration file name from Streamlit secrets
    secrets_name = st.secrets.get("secrets_config", {}).get("secrets_name", ".streamlit/secrets.toml")

    # Ensure the file has the correct path
    if not secrets_name.endswith(".toml"):
        secrets_name = f".streamlit/{secrets_name}.toml"
    
    # Convert to absolute path
    absolute_path = os.path.abspath(secrets_name)

    # Check if the file exists
    if not os.path.isfile(absolute_path):
        st.error(f"The configuration file '{absolute_path}' was not found. Please check the path and file name.")
        return None

    # Load configuration from the TOML file
    try:
        db_config = toml.load(absolute_path)["db_config"]
    except KeyError:
        st.error("The 'db_config' section was not found in the configuration file.")
        return None
    except Exception as e:
        st.error(f"Error loading the configuration file: {e}")
        return None
    
    return db_config
