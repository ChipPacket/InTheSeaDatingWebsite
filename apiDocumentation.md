# InTheSea API Documentation

## About the API
The purpose of this API is to store user data for our dating website 'InTheSea' and store information the admins to maintain our website.

Version: 1.0

More Info: https://github.com/ChipPacket/InTheSeaDatingWebsite/blob/main/README.md

## Connecting to the API

### API Host
API is local hosted: http://127.0.0.1:5000


## Security

### apiKey
apiKey

Identifier: X-API-Key
Every request requires an API key. 
To get an API key:
<ol>
    <li>run db_creation.py</li>
    <li>run auto_populate.py</li>
    <li>run populate_apikeys.py</li>
    <li>run showkeys.py to get the api keys</li>
    <li>copy key into clientpages/scripts/const.js & adminpages/scripts/const.js</li>
    <li>run app.py and visit website 🎉</li>
</ol>

## Contents
### Key
All of the post, get, put and delete functions require an api key which can be found by running showkeys.py
However, the login functions do not require a key

```@require_api_key```

<br>

## API Resources
CREATE, READ, UPDATE, DELETE
```
api.add_resource(UserAPI, "/api/users")

api.add_resource(AdminAPI, "/api/admins")

api.add_resource(BlogPostAPI, "/api/blogPosts")

api.add_resource(ReportAPI, "/api/reports")
```
CREATE
```
api.add_resource(LoginAPI, "/api/login")

api.add_resource(AdminLoginAPI, "/api/admin/login")
```
### login Recources

The login resources are used to get the user or admin id without having the passwords being passed to the front end for added security


### Create
post(self)

### Read
get(self)

### Update
put(self)

### Delete
delete(self)

