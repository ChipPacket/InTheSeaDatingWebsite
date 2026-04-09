from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from models import db, User, Admin, BlogPost, Report
from datetime import datetime
from auth import require_api_key
from flask_cors import CORS





# Create a Flask application instance
app = Flask(__name__)
CORS(app)

# Configure the SQLite database location
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ITS.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize the database with the app
db.init_app(app)

# Create API instance
api = Api(app)

class UserAPI(Resource):
    # GET method retrieves all Users from the database
    @require_api_key  # Apply middleware to GET requests
    def get(self):
        users = User.query.all()
        user_list = []

        # Loop through each user and prepare data for JSON response
        for user in users:
            user_data = {
                "id": user.userID,
                "firstName": user.firstName,
                "lastName": user.lastName,
                "birthday": user.birthday,
                "email": user.email,
                "mobile": user.mobileNo,
                "ownGender": user.ownGender,
                "attractedGender": user.attractedGender,
                "profileContent": user.profileContent,
                "password": user.password,
                "activeUser": user.activeUser,
                "q1": user.q1,
                "q2": user.q2,
                "q3": user.q3,
                "a1": user.a1,
                "a2": user.a2,
                "a3": user.a3,
                "image": user.image
            }
            user_list.append(user_data)

        # Return the User list in JSON format
        return jsonify(user_list)
    
    # POST method to add a new User
    @require_api_key  # Apply middleware to POST requests
    def post(self):
        data = request.get_json()

        required_fields = [
            "firstName", "lastName", "birthday", "email", "mobileNo",
            "ownGender", "attractedGender", "profileContent", "password", "image"
        ]
        if not data or any(field not in data for field in required_fields):
            return {"error": "Missing required fields"}

        new_user = User(
            firstName=data["firstName"],
            lastName=data["lastName"],
            birthday=datetime.strptime(data["birthday"], "%Y-%m-%d").date(),
            email=data["email"],
            mobileNo=data["mobileNo"],
            ownGender=data["ownGender"],
            attractedGender=data["attractedGender"],
            profileContent=data["profileContent"],
            password=data["password"],
            activeUser=True,
            image=data["image"],
            q1=data["q1"],
            q2=data["q2"],
            q3=data["q3"],
            a1=data["a1"],
            a2=data["a2"],
            a3=data["a3"]
        )

        db.session.add(new_user)
        db.session.commit()

        return {"message": "New user added successfully!"}

    # PUT method to update an existing user
    @require_api_key  # Apply middleware to PUT requests
    def put(self):
        data = request.json
        user_id = data.get("id")

        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}

        # Update user details
        user.firstName=data["firstName"]
        user.lastName=data["lastName"]
        user.birthday=datetime.strptime(data["birthday"], "%Y-%m-%d").date()
        user.email=data["email"]
        user.mobileNo=data["mobileNo"]
        user.ownGender=data["ownGender"]
        user.attractedGender=data["attractedGender"]
        user.profileContent=data["profileContent"]
        password = data.get("password")
        if password:
            user.password = password
        user.activeUser=data["activeUser"]
        user.image=data["image"]
        user.q1=data["q1"]
        user.q2=data["q2"]
        user.q3=data["q3"]
        user.a1=data["a1"]
        user.a2=data["a2"]
        user.a3=data["a3"]

        # Commit the changes
        db.session.commit()

        return {"message": "User updated successfully!"}

    #DELETE method removes a User by ID
    @require_api_key  # Apply middleware to DELETE requests
    def delete(self):
        data = request.json
        user_id = data.get("id")

        user = User.query.get(user_id)
        if not user:
            return {"error": "User not found"}

        # Delete the user and commit changes
        db.session.delete(user)
        db.session.commit()

        return {"message": "User deleted successfully!"}

api.add_resource(UserAPI, "/api/users")

class AdminAPI(Resource):
    # GET method retrieves all Admins from the database
    @require_api_key  # Apply middleware to GET requests
    def get(self):
        admins = Admin.query.all()
        admin_list = []

        # Loop through each user and prepare data for JSON response
        for admin in admins:
            admin_data = {
                "id": admin.adminID,
                "firstName": admin.firstName,
                "lastName": admin.lastName,
                "birthday": admin.birthday,
                "email": admin.email,
                "permissionLevel": admin.permissionLevel
            }
            admin_list.append(admin_data)

        # Return the User list in JSON format
        return jsonify(admin_list)
    
    # POST method to add a new User
    @require_api_key  # Apply middleware to POST requests
    def post(self):
        data = request.get_json()

        required_fields = [
            "firstName", "lastName", "birthday", "email", "permissionLevel", "password"
        ]
        if not data or any(field not in data for field in required_fields):
            return {"error": "Missing required fields"}

        new_admin = Admin(
            firstName=data["firstName"],
            lastName=data["lastName"],
            birthday=datetime.strptime(data["birthday"], "%Y-%m-%d").date(),
            email=data["email"],
            permissionLevel=data["permissionLevel"],
            password=data["password"]
        )

        db.session.add(new_admin)
        db.session.commit()

        return {"message": "New user added successfully!"}

    # PUT method to update an existing user
    @require_api_key  # Apply middleware to PUT requests
    def put(self):
        data = request.json
        admin_id = data.get("id")

        admin = Admin.query.get(admin_id)
        if not admin:
            return {"error": "Admin not found"}

        # Update Admin details
        admin.firstName=data["firstName"]
        admin.lastName=data["lastName"]
        admin.birthday=datetime.strptime(data["birthday"], "%Y-%m-%d").date()
        admin.email=data["email"]
        admin.permissionLevel=data["permissionLevel"]
        admin.password=data["password"]

        # Commit the changes
        db.session.commit()

        return {"message": "Admin updated successfully!"}

    #DELETE method removes a Admin by ID
    @require_api_key  # Apply middleware to DELETE requests
    def delete(self):
        data = request.json
        admin_id = data.get("id")

        admin = Admin.query.get(admin_id)
        if not admin:
            return {"error": "Admin not found"}

        # Delete the admin and commit changes
        db.session.delete(admin)
        db.session.commit()

        return {"message": "Admin deleted successfully!"}

api.add_resource(AdminAPI, "/api/admins")

class BlogPostAPI(Resource):
    # GET method retrieves all BlogPosts from the database
    @require_api_key  # Apply middleware to GET requests
    def get(self):
        blogPosts = BlogPost.query.all()
        blogPost_list = []

        for blogPost in blogPosts:
            blogPost_data = {
                "id": blogPost.blogID,              
                "adminID": blogPost.adminID,        
                "author": blogPost.authors,        
                "title": blogPost.title,
                "content": blogPost.content,
                "image": blogPost.image,
                "dateOfPublish": blogPost.dateOfPublish
            }
            blogPost_list.append(blogPost_data)

        return jsonify(blogPost_list)
    
    # POST method to add a new User
    @require_api_key  # Apply middleware to POST requests
    def post(self):
        data = request.get_json()

        required_fields = [
            "adminID", "authors", "title", "content", "image", "dateOfPublish"
        ]
        if not data or any(field not in data for field in required_fields):
            return {"error": "Missing required fields"}

        new_blogPost = BlogPost(
            adminID=data["adminID"],
            authors=data["authors"],
            title=data["title"],
            content=data["content"],
            image=data["image"],
            dateOfPublish=datetime.strptime(data["dateOfPublish"], "%Y-%m-%d").date()
        )

        db.session.add(new_blogPost)
        db.session.commit()

        return {"message": "New BlogPost added successfully!"}

    # PUT method to update an existing Post
    @require_api_key  # Apply middleware to PUT requests
    def put(self):
        data = request.json
        blogPost_id = data.get("id")

        blogPost = BlogPost.query.get(blogPost_id)
        if not blogPost:
            return {"error": "BlogPost not found"}

        # Update BlogPost details
        blogPost.adminID=data["adminID"]
        blogPost.author=data["author"]
        blogPost.title=data["title"]
        blogPost.content=data["content"]
        blogPost.image=data["image"]
        if "dateOfPublish" in data and data["dateOfPublish"]:
            blogPost.dateOfPublish = datetime.strptime(data["dateOfPublish"], "%Y-%m-%d").date()
        

        # Commit the changes
        db.session.commit()

        return {"message": "BlogPost updated successfully!"}

    #DELETE method removes a BlogPost by ID
    @require_api_key  # Apply middleware to DELETE requests
    def delete(self):
        data = request.json
        blogPost_id = data.get("id")

        blogPost = BlogPost.query.get(blogPost_id)
        if not blogPost:
            return {"error": "BlogPost not found"}

        # Delete the blogPost and commit changes
        db.session.delete(blogPost)
        db.session.commit()

        return {"message": "BlogPost deleted successfully!"}

api.add_resource(BlogPostAPI, "/api/blogPosts")

class ReportAPI(Resource):
    # GET method retrieves all Reports from the database
    @require_api_key  # Apply middleware to GET requests
    def get(self):
        reports = Report.query.all()
        report_list = []

        # Loop through each report and prepare data for JSON response
        for report in reports:
            report_data = {
                "id": report.reportID,
                "reportedUserID": report.reportedUserID,
                "reason": report.reason,
                "comment": report.comment,
                "adminID": report.adminID,
                "adminDecision": report.adminDecision,
                "adminComment": report.adminComment
            }
            report_list.append(report_data)

        # Return the Report list in JSON format
        return jsonify(report_list)
    
    # POST method to add a new Report
    @require_api_key  # Apply middleware to POST requests
    def post(self):
        data = request.get_json()

        required_fields = [
            "reportedUserID", "reason", "comment", "adminID", "adminDecision",
            "adminComment"
        ]

        if not data or any(field not in data for field in required_fields):
            return {"error": "Missing required fields"}

        new_report = Report (
            reportedUserID=data["reportedUserID"],
            reason=data["reason"],
            comment=data["comment"],
            adminID=data["adminID"],
            adminDecision=data["adminDecision"],
            adminComment=data["adminComment"]
        )

        db.session.add(new_report)
        db.session.commit()

        return {"message": "New Report added successfully!"}

    # PUT method to update an existing user
    @require_api_key  # Apply middleware to PUT requests
    def put(self):
        data = request.json
        report_id = data.get("id")

        report = Report.query.get(report_id)
        if not report:
            return {"error": "Report not found"}

        # Update user details
        report.reportedUserID=data["reportedUserID"]
        report.reason=data["reason"]
        report.comment=data["comment"]
        report.adminID=data["adminID"]
        report.adminDecision=data["adminDecision"]
        report.adminComment=data["adminComment"]
        
        # Commit the changes
        db.session.commit()

        return {"message": "Report updated successfully!"}

    #DELETE method removes a Report by ID
    @require_api_key  # Apply middleware to DELETE requests
    def delete(self):
        data = request.json
        report_id = data.get("id")

        report = Report.query.get(report_id)
        if not report:
            return {"error": "Report not found"}

        # Delete the Report and commit changes
        db.session.delete(report)
        db.session.commit()

        return {"message": "User deleted successfully!"}

api.add_resource(ReportAPI, "/api/reports")

# Slight bit of security
class LoginAPI(Resource):
    def post(self):

        #get user inputs
        data = request.get_json()

        #get the email and password
        email = data.get("email")
        password = data.get("password")

        #check all data is there
        if not email or not password:
            return {"error": "Email and password required"}

        #find user id of matching email
        user = User.query.filter_by(email=email).first()

        if not user:
            return {"error": "User not found :("}

        #check if password mismatch
        if user.password != password:
            return {"error": "Invalid password :("}

        #return user id and email if sucess
        return {
            "message": "Login successful yay",
            "user": {
                "id": user.userID,
                "email": user.email
            }
        }

api.add_resource(LoginAPI, "/api/login")

class AdminLoginAPI(Resource):
    def post(self):

        #get admin inputs
        data = request.get_json()

        #get the admin ID and password
        adminID = data.get("adminId")
        password = data.get("password")

        #check all data is there
        if not adminID or not password:
            return {"error": "Admin ID and password required"}

        #find admin id of matching admin ID
        admin = Admin.query.filter_by(adminID=adminID).first()

        if not admin:
            return {"error": "Admin not found :("}

        #check if password mismatch
        if admin.password != password:
            return {"error": "Invalid password :("}

        #return admin id if sucess
        return {
            "message": "Login successful yay",
            "admin": {
                "id": admin.adminID
            }
        }

api.add_resource(AdminLoginAPI, "/api/admin/login")

if __name__ == "__main__":
    app.run(debug=True)
