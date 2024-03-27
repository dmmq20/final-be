import subprocess

command = ['psql', '-f', './setup.sql']

try:
    subprocess.run(command, check=True)
    print("Setup SQL file executed successfully.")

    from app.db.tables_setup import drop_tables, create_tables, insert_test_documents, insert_test_users, insert_test_comments
    drop_tables()
    create_tables()
    insert_test_users()
    insert_test_documents()
    insert_test_comments()

    print("Database setup completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error executing setup SQL file: {e}")
except Exception as e:
    print(f"Error setting up the database: {e}")
