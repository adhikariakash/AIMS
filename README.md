AIMS python project
===============
Introduction
----
A console application which has a main page with 3 different types of members i.e ADMIN , SUPERVISING TEAM, EMPLOYEE with their respective features, where every option takes user to their respective roles class and introduce to their features. The project is using sqlite database to store data.
### Project Doc
Project documentation link : https://docs.google.com/document/d/1uYiBGuXl1rxp36zle6d2NupgONPciq7UcSFTuvQuhHo/edit
Setup for Running the Project
---
```   
1. Open the project AIMS
2. Run pythonn file 'Dashboard.py'
    -> python Dashboard.py
```
Credentials to run the project :
---
```
1. ADMIN:
   Username: admin
   Password: pass
2. Employee:
   Username: raj
   Password: 123456
3. Supervising team:
   Username: teamA
   Password: 123456
```
Setup for Running test cases
---
```
For running test cases
    -> coverage run -m pytest
For coverage result
    ->  coverage report -m Admin.py Dashboard.py Repository.py Login.py SupervisingTeam.py Employee.p
For storing the test result locally in html format run these commands
    -> coverage run --source=. -m unittest discover
    -> coverage html
```
Dependencies
----
1. **sqlite3**:
    - **connect**: generate connection object with database
2. **coverage**:
    - **pycoverage**: framework for checking coverage
3. **pytest**:
    - **pytest**: framework for running unit test cases
4. **cryptography**:
    python3 -m pip install cryptography
5. **pandas**:
    python3 -m pip install pandas
6. **graph**:
    python3 -m pip install mathplotlib
