from app import db, app
from models import User, Admin, BlogPost, Report

with app.app_context():
    db.create_all()
    print("Database tables created successfully!")

