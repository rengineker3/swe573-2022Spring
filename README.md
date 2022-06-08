# swe573-2022Spring
A software project for BOUN SWE573 Class. 

### BOGAZİCİ UNİVERSITY, 2022 SPRING SWE 573 CLASS PROJECT

This is a Co-Learning and Hangout website where users can share their knowledge and interest. For more details please click [Wiki](https://github.com/rengineker3/swe573-2022Spring/wiki) 

To see deployment: [LearningLand](http://ec2-3-92-141-216.compute-1.amazonaws.com) 
  
 ## How to Install Project? 
 
 `git clone https://github.com/rengineker3/swe573-2022Spring.git`

* Project needs postgresql and docker. 
* Start with create your virtual environment with:
`python3 -m venv myvenv`
`source myvenv/bin/activate`  
* Install: `pip install -r requirements.txt`
* Create Database: 
`docker-compose up --build`
`docker-compose start db` 
`docker exec -it core_db bash`
`psql -U postgres`
`CREATE DATABASE learningland;`  
`/l`  (to check if the database is created).

* After database creation run this command:  
`docker-compose up` Check if the containers are up and running.
* Go to your local host port 80 in the browser, 127.0.0.1:80

 
 

