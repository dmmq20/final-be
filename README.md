# final-be

git clone https://github.com/dmmq20/final-be.git

cd final-be

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt

touch .env

echo DATABASE_URL=postgresql://@localhost/fastapi_db > .env

python setup_dbs.py

uvicorn app.main:app --reload
