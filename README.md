
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

Project Setup Update: 

1. install pymongo, 
    pip install pymongo
2. install pymongo[srv]
    pip install "pymongo[srv]"
3. run command
    sed -i -e 's/\r$//' run.sh
4. run command
    ./run.sh
The login and register page should appears. 


Brainstorming:

idea_1:
Map Social, we intend to create a map software that will allow users post tasks and earn income by finishing other people's posting tasks on this software. The over all idea was to make people make money form helping others and earn some easy money. The over finalized map may look similar to style of Pokemon Go, combine 3D map with small tags and windows showing near by tasks to users. We need data base to store User info, map data, task requirements, and Paying record for this project. 

idea_2:
Security software, users can use this software to protect their security at any time, users can turn on the password every 15 minutes to enter to confirm the status of their security. If the user is in danger, the location will be shared to the user's friends and people around them. We need user permission to user local position for Google map data and user data should be stored in data base for validation usage.

idea_3: 
A Quora/piazza like website for NYU. Professors and students, when need interns or team members to complete a research/project, can post the information on the website to recruit helpers, and people who are interested can send out their resumes and other materials, and finally the leader of the project can choose the most suited one to help him/her. And the professors or students could post pictures, article, needs categorize by tags to show their current working progress. The project in this case means larger independent projects rather than some small class projects. This project may be mentored by PHD student form civil engineering department and been used for future in class project match
and PHD students that need to find other students that might interested in collaberate the project.

idea_4:
A software for people to find gamers to play with them by paying a small amount of money. The people who are employed on the software are skilled and experienced players of specific games. The users can be starters who simply wants to comprehend the experience of new games or gamers who need coaches to give them some suggestions about how to improve gaming skills. Users submit their requests and the system will create orders. After employees accept the orders, the system will send the players imformation to the users to choose.


We pick idea 3 as our final project. We hope to realize the five functions of users posting information, commenting and replying, logging in, and searching in the project. The entire project will be composed by 4 major web pages, indluding user end topics/projects visualizing page, a visualize page for specific topics/projects, a manager page where web controller could make modifications or delete any of the project posted. We plan to finished the project by steps. 

In the first step, we want to enable users to publish text and picture information on the platform in the project. Meaning we need a user input page and a index page that shows the posted in formation. In the user editor page, we want to include functionalities of Text editing includes the possibility to post links, adjust text size, and adjust fonts. We will implement the storage of published text information through mongoDB.

