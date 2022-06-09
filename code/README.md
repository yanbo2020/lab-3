YAAQOB ABDLSATTAR HAMID ABDULQADER -201932130146 (leader)
RADMAN ABDULNASER ABDULHABEB SHAMSAN-201932130140
Mutumba Jonathan -201932130136
ABBDULHAKIM ALI HASSAN-201932130107
AL-ASBHI YOUSF NAJEEB AMEEN ABDULJABAR-201832130105
Lab3: Persistence Ignorance
Introduction:

In main point of this lab is to understand the repository pattern and the service layer pattern , also get to know why it is important to separate business logic from data storage techniques.

What we will be applying is a non database strategy while implementing the repository pattern by defining a class PickleRepository. 
Materials and Methods:
1-Use the repository 
2-Use the service layer 
3-Pickle library 
4-Pytest 

Results:





Discussions:
What is the difference between the textbook test services.py and my test services.py? 
1_Well in your my test services at     you stored the batch as a dictionary  but in the textbook it was stored as a list 
2 - 


2-Has the service layer been affected after we have chosen to use another implementation for the Repository Pattern? Can we say that the service layer is ignorant of the persistence? 
Its not effected and the  ignorant of the persistence was applied to SQLAlchemy
3-What is the benefit of separating business logic from infrastructure concerns? Where is the business logic defined, and where is the infrastructure defined? Tell me the Python file name(s).
The benefit is that when  its separated it will be easier to test and modify  , not separating it will lead in slowing down the unit tests or making changes hard  



