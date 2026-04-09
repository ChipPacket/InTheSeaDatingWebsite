# InTheSea API Documentation

## About the API
These endpoints constitute the functionality exposed by Bungie.net, both for more traditional website functionality and for connectivity to Bungie video games and their related functionality. ?????????????????/

Version: 1.0

More Info: https://github.com/ChipPacket/InTheSeaDatingWebsite

## Connecting to the API

### Server Endpoint
API Root Path: https://www.bungie.net/Platform
The endpoint for accessing the Bungie.net API. You probably guessed that already. ?????????????????????


## Security

### apiKey
apiKey
Identifier: X-API-Key
Every request requires an API key. To get an API key:
<ol>
    <li>run db_creation.py  delete??????????????????????????</li>
    <li>run auto_populate.py ??????????????</li>
    <li>run populate_apikeys.py</li>
    <li>run showkeys.py to get the api keys</li>
    <li>copy key into clientpages/scripts/const.js & adminpages/scripts/const.js</li>
    <li>run app.py and visit website 🎉</li>
</ol>

## Contents
### Key
Stuff about the use of api key middleware etc

@require_api_key

<br>

### Create
post(self)



Examples:

|Example|Code|
|:-|:-|
|User makes an account|```code```|
|User add details to their account|```code```|
|Creating an admin account|```code```|

<br>

### Read
get(self)

|Example|Code|
|:-|:-|
|All user profiles|```code```|
|All blog posts|```code```|
|Verifying login credentials|```code```|

<br>

### Update
put(self)
|Example|Code|
|:-|:-|
|Users updating their profile|```code```|
|Admins updating their decision to ban|```code```|

<br>

### Delete
delete(self)


|Example|Code|
|:-|:-|
|User wants to delete their account|```code```|
|User gets banned|```code```|