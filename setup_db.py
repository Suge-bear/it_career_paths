# setup_db.py

from app import db, app
from models import User, CareerPath

with app.app_context():
    db.create_all()
    print("✅ Database tables created!")
