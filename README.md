
# swe_project
An example flask rest API server, for SE Fall 2022.

To build production, type `make prod`.

To create the env for a new developer, run `make dev_env`.

Tech Stack used for this project:
Testing: pytest
Server: Flask && flask-restx
Lint: flake8
Database: MongoDB
CI/CD: Github Action
Cloud deployment: Heroku
Frontend: React
###################################

Backend deployed to Heroku at
https://project-finder.herokuapp.com/

Backend Github Link: https://github.com/BowenGong2000/swe_project
Frontend Github Link: https://github.com/FantasiA10/Project-matcher

## Project Setup Update: 

1. install pymongo, 
    pip install pymongo
2. install pymongo[srv]
    pip install "pymongo[srv]"
3. install passlib for password encyption
    pip install passlib
4. run command
    sed -i -e 's/\r$//' server.sh
5. run command
    for Windows users: 
        ./server.sh

    for Mac users: 
        ./run.sh-e
        
Go to http://127.0.0.1:5000
The login and register page should appears. 

To login to home page user should register a new account, and use that account to login to homepage. 

## Requirements

### User endpoints:
- Signup (add a user)
- Login (verify credential)
- Get info of a user
- List all registered users
- Delete a user
- Edit/Update user info
- Edit profile photo

### Projects endpoints:
- List all available projects
- Get info of a project
- Create a project
- Delete a project
- Approve a project (admin only)
- Upload and download project files

### Application endpoints:
- List all applications of a user
- Get info of a application
- Create a application for a specific project
- Send user email notifications
- Cancel/Delete a application

### Flow Chart:
![alt text](static/images/flowchart.png)

resources of code for UI:
head protray https://www.deviantart.com/karmaanddestiny/art/Default-user-icon-4-858661084
form comtribution: https://github.com/JeetSaru/Responsive-HTML-Table-With-Pure-CSS---Web-Design-UI-Design

Checking if Autodeployment works 
