import subprocess

from app.database import create_tables, drop_tables, insert_test_documents, insert_test_users

command = ['psql', '-f', './setup.sql']

try:
    subprocess.run(command, check=True)
    print("Setup SQL file executed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing setup SQL file: {e}")


drop_tables()
create_tables()
insert_test_users()
insert_test_documents()
