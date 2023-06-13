# Volopay Assignment
Volopay Assignment for Backend Engineer Internship.

I have used Pyhton - Flask Framework with PostgeSQL database. 
To execute the application on your machine follow these steps:

1. Create a virtual environment with requirements.txt file. VSCode will do it for you if you open the requirements.txt file in VSCode.
2. Setup the DB_URL in Config.py file. DB URL should look like this: "postgresql://<username>:<password>@<db_host>:<db_port>/<db_name>"
3. After this, execute the following file: backend>database>models.py https://github.com/shyamsar30/volopay-assignment/blob/main/backend/database/models.py. This will create the database table.
4. Now import the given Data.csv file to it. I have done it directly using DBever.
5. Now upon executing the app.py file, you will see the url on the console. 
6. I have documented code with Swagger UI. You can use it to test the APIs.
