# Final Backend Project

This repository contains the backend code for the final project.

## Setup Instructions

Follow these steps to set up the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/dmmq20/final-be.git
   cd final-be
   ```

2. Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file and configure the database URL:

   ```bash
   touch .env
   echo DATABASE_URL=postgresql://@localhost/fastapi_db > .env
   ```

5. Set up the database:

   ```bash
   python setup_dbs.py
   ```

## Running the Server

To start the server, run the following command:

```bash
uvicorn app.main:app --reload
```

OR

```bash
python main.py
```

This will start the server with auto-reloading enabled, making it convenient for development.

## Testing

To run the tests, run the following command:

```bash
pytest
```
