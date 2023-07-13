# jumpingminds_elevator


Problem Statement
1. An elevator System having n elevators and all the elevators work from a single button on each floor 
2. The system has to assign the most optimal elevator to the user according to their request.


Assumptions
1. Assume the API calls which make the elevator go up/down or stop will reflect immediately. When the API to go up is called, you can assume that the elevator has already reached the above floor.


Thought Process
1. Create n elevators object and assign to a single elevator system
2. We will get a list of request from elevator request API
3. Find the closest operational elevator from the request list and assign elevator to that request
4. Process the request and remove the request from the list

API Contacts:
https://docs.google.com/document/d/1xYEbY_y5ZbzNLhYKhQu-G5i8qDI9t080PPgfve1BIWQ/edit?usp=sharing

Steps to Setup:
1. Create a virtual environment
2. Install python and pip
3. Run command 
    pip install -r requirements.txt
4. python manage.py makemigrations
5. python manage.py migrate
6. python manage.py runserver 

Modification Areas:
1. Use env.yml file to store the database connection url
2. Use primary key (pk) instead of query params