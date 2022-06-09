
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
![image](https://user-images.githubusercontent.com/75038987/172804751-a11f5a00-eaf3-4d22-a439-3e51ec3f2bd9.png)
![image](https://user-images.githubusercontent.com/75038987/172804792-ef35ef84-a2fc-4322-8f79-e65dc5cacee7.png)





Discussions:

1-Has the service layer been affected after we have chosen to use another implementation for the Repository Pattern? Can we say that the service layer is ignorant of the persistence? 
Its not effected and the  ignorant of the persistence was applied to SQLAlchemy


2-What is the benefit of separating business logic from infrastructure concerns? Where is the business logic defined, and where is the infrastructure defined? Tell me the Python file name(s).
The benefit is that when  its separated it will be easier to test and modify  , not separating it will lead in slowing down the unit tests or making changes hard  



