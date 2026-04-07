from app import app, db
from models import User, Admin, BlogPost, Report
from datetime import date

# List of users to add
users = [
    {
        "firstName": "John",
        "lastName": "Doe",
        "birthday": date(1995, 5, 14),
        "email": "john.doe@example.com",
        "mobileNo": "07123456789",
        "ownGender": "Male",
        "attractedGender": "Female",
        "profileContent": "Love travelling and music",
        "password": "hashedpassword123",
        "activeUser": True
    },
    {
        "firstName": "Jane",
        "lastName": "Smith",
        "birthday": date(1998, 8, 22),
        "email": "jane.smith@example.com",
        "mobileNo": "07234567890",
        "ownGender": "Female",
        "attractedGender": "Male",
        "profileContent": "Gym lover and foodie",
        "password": "hashedpassword456",
        "activeUser": True
    },
    {
        "firstName": "Alex",
        "lastName": "Taylor",
        "birthday": date(2000, 1, 10),
        "email": "alex.taylor@example.com",
        "mobileNo": "07345678901",
        "ownGender": "Non-binary",
        "attractedGender": "All",
        "profileContent": "Tech enthusiast",
        "password": "hashedpassword789",
        "activeUser": True
    }
]

admins = [
    {
        "firstName": "Hamish",
        "lastName": "Mitchell",
        "birthday": date(2006, 3, 22),
        "email": "Hamishgmitchell@gmail.com",
        "permissionLevel": "Max"
    },
    {
        "firstName": "Micheal",
        "lastName": "Bell",
        "birthday": date(2007, 5, 17),
        "email": "michaelbell@hotmail.com",
        "permissionLevel": "Max"
    }
]

reports = [
    {
        "reportedUserID": 2,
        "reason": "Inappropriate content",
        "comment": "User posted offensive messages",
        "adminID": None,
        "adminDecision": None,
        "adminComment": None
    },
    {
        "reportedUserID": 3,
        "reason": "Spam",
        "comment": "Repeated promotional messages",
        "adminID": None,
        "adminDecision": None,
        "adminComment": None
    },
    {
        "reportedUserID": 1,
        "reason": "Fake profile",
        "comment": "Profile seems suspicious",
        "adminID": None,
        "adminDecision": None,
        "adminComment": None
    }
]

blog_posts = [
    {
        "adminID": 1,
        "authors": "Hamish Mitchell",
        "title": "Welcome to Our Platform",
        "content": "This is the first blog post introducing our app.",
        "image": "welcome.jpg",
        "dateOfPublish": date(2024, 1, 1)
    },
    {
        "adminID": 2,
        "authors": "Michael Bell",
        "title": "Safety Tips",
        "content": "Here are some tips to stay safe while using the app.",
        "image": "safety.jpg",
        "dateOfPublish": date(2024, 2, 10)
    },
    {
        "adminID": 2,
        "authors": "Maddie Gee",
        "title": "New Features Released",
        "content": "We've added exciting new features!",
        "image": "features.jpg",
        "dateOfPublish": date(2024, 3, 15)
    }
]

with app.app_context():

    for user_data in users:
    #create user
        new_user = User(
            firstName=user_data["firstName"],
            lastName=user_data["lastName"],
            birthday=user_data["birthday"],
            email=user_data["email"],
            mobileNo=user_data["mobileNo"],
            ownGender=user_data["ownGender"],
            attractedGender=user_data["attractedGender"],
            profileContent=user_data["profileContent"],
            password=user_data["password"],
            activeUser=user_data["activeUser"]
        )

        # Add to database
        db.session.add(new_user)

    for admin_data in admins:
        new_admin = Admin(
            firstName=admin_data["firstName"],
            lastName=admin_data["lastName"],
            birthday=admin_data["birthday"],
            email=admin_data["email"],
            permissionLevel=admin_data["permissionLevel"]
        )
        db.session.add(new_admin)

    for report_data in reports:
            new_report = Report(
                reportedUserID=report_data["reportedUserID"],
                reason=report_data["reason"],
                comment=report_data["comment"],
                adminID=report_data["adminID"],
                adminDecision=report_data["adminDecision"],
                adminComment=report_data["adminComment"]
            )
            db.session.add(new_report)

    for post_data in blog_posts:
        new_post = BlogPost(
            adminID=post_data["adminID"],
            authors=post_data["authors"],
            title=post_data["title"],
            content=post_data["content"],
            image=post_data["image"],
            dateOfPublish=post_data["dateOfPublish"]
        )
        db.session.add(new_post)


    # update database
    db.session.commit()

    print("Database populated successfully!")