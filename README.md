This coding challenge was for the most part prettyy straight forward. Initially after reading the project details, the main task that stood out for me the most was 
* 1) Linking the DB with the model if it wasnt already done so. 
* 2) Populating the Db with test data 
* 3) Setting up the API end points to return Data 
* 4) Creating the front end html to consume the API

Task 1 was relativly simple to complete, all it required was creating a serializer class
Task 2 required creating a json Document to populate the DB with and then running python manager.py loaddata <file-name>
Task 3 and task 4 took the most of my time, maily because of how I had done Task 3. In task 3 I initially create my API end points using APIView for my model but ended up
changing it to ViewSet thinking it would be easier. When I got to task 4 I had troubling figureing out how to link the template files to the ViewSet. I ended up reverting my code to utilize the APIView again and creating a TemplateView to display the data.

-Derek