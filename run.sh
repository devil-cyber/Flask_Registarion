pip install virtualenv
source venv/bin/activate
pip install -r requirements.txt
sqlite3 database.db < schema.sql
python app.py