## Template For Role Based Access Control Using Flask & Mongo
To use this role-based access control template

---
1. Clone this repository to local computer

2. Rename the directory to reflect the new project name

3. Delete .git folder

4. Create a new virtual environment 
    - Windows:  ```python -m venv ./venv```
    - Mac:  ```python3 -m venv ./venv```

5. Activate the new virtual environment
   - Windows:  ```.\venv\Scripts\activate```
   - Mac:  ```source ./venv/bin/activate```

6. Install the dependencies ```pip install -r requirements.txt```

7. Make a new repository by running ```git init``` in the folder.

8. Track all the files in the new local repository ```git add .```

9. Make the first commit of this new project ```git commit -m 'first commit of <project name> from flask_template```

10. On Github, create a new repository. *DO NOT* initialize it

11. Connect the local repository to the new Github repository ```git remote add origin <<repository_URL>>```

12. Create and change to a new local development branch ```git checkout b development```

13. Continue working with the project as you normally would.


***


### Create an account on MongoDB Atlas
[MongoDB Atlas] https://www.mongodb.com/cloud/atlas/


### Create an .env file

1. In the project root, create a new file named .env

2.  You can get the Mongo connection should be completed with values from your database user in Atlas.

MONGO = "mongodb+srv://*REPLACE_ME_WITH_YOUR_DATABASE_USER:REPLACE_ME_WITH_YOUR_DATABASE_USER_PASSWORD*@cluster0.upbc3.mongodb.net/*REPLACE_ME_WITH_YOUR_DATABASE_NAME*?retryWrites=true&w=majority"

3.  Create a  secret key.
SECRET_KEY = "*REPLACE_ME_WITH_YOUR_SECRET_KEY_HERE*"
