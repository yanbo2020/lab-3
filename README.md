
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
REPOSITORY.PY
![image](https://user-images.githubusercontent.com/75038987/172806123-b821c836-3b5d-4dec-9e54-4f720b1afbe7.png)

![image](https://user-images.githubusercontent.com/75038987/172806165-d7b0d047-f655-490e-89bd-51228ea5401c.png)





Discussions:




1-Has the service layer been affected after we have chosen to use another implementation for the Repository Pattern? Can we say that the service layer is ignorant of the persistence? 
Its not effected and the  ignorant of the persistence was applied to SQLAlchemy


2-What is the benefit of separating business logic from infrastructure concerns? Where is the business logic defined, and where is the infrastructure defined? Tell me the Python file name(s).
The benefit is that when  its separated it will be easier to test and modify  , not separating it will lead in slowing down the unit tests or making changes hard  




