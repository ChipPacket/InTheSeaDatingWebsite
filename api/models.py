from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# User model
class User(db.Model):
    userID = db.Column(db.Integer, primary_key=True)  # Unique ID for each user
    firstName = db.Column(db.String(50), nullable=False)  
    lastName = db.Column(db.String(50), nullable=False)  
    birthday = db.Column(db.Date, nullable=False)  
    email = db.Column(db.String(150), nullable=False)
    mobileNo = db.Column(db.String(20), nullable=False)  
    ownGender = db.Column(db.String(50), nullable=False)  
    attractedGender = db.Column(db.String(50), nullable=False)
    profileContent = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    activeUser = db.Column(db.Boolean, default=True)

class Admin(db.Model):
    adminID = db.Column(db.Integer, primary_key=True)  # Unique ID for each Admin
    firstName = db.Column(db.String(50), nullable=False)  
    lastName = db.Column(db.String(50), nullable=False)  
    birthday = db.Column(db.Date, nullable=False)  
    email = db.Column(db.String(150), nullable=False)
    permissionLevel = db.Column(db.String(50), nullable=False)

class Report(db.Model):
    reportID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Unique ID for each Report
    reportedUserID = db.Column(db.Integer, nullable=False)  #UsersID
    reason = db.Column(db.String(50), nullable=False)  
    comment = db.Column(db.String(200), nullable=True)  
    adminID = db.Column(db.String(150), nullable=True)
    adminDecision = db.Column(db.String(50), nullable=True)
    adminComment = db.Column(db.String(200), nullable=True)

class BlogPost(db.Model):
    blogID = db.Column(db.Integer, primary_key=True, autoincrement=True)  # Unique ID for each Blog
    adminID = db.Column(db.Integer, nullable=False)  #AdminsID responsable
    authors = db.Column(db.String(50), nullable=False)  
    title = db.Column(db.String(200), nullable=True)  
    content = db.Column(db.String(150), nullable=True)
    image = db.Column(db.String(50), nullable=True)
    dateOfPublish = db.Column(db.Date, nullable=False) 

class APIKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(64), unique=True, nullable=False)
    owner = db.Column(db.String(50), nullable=False)
    request_count = db.Column(db.Integer, default=0)
    rate_limit = db.Column(db.Integer, default=1000)
