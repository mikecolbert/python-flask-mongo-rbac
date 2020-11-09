import pymongo
import datetime

## necessary for python-dotenv ##
APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

mongo = os.getenv('MONGO')

client = pymongo.MongoClient(mongo)

db = client['recipe_app']

users = db['users']
roles = db['roles']
recipes = db['recipes']
categories = db['categories']


def add_role(role_name):
    role_data = {
        'Role Name': role_name
    }
    return roles.insert_one(role_data)


def add_category(category_name):
    category_data = {
        'Category Name': category_name
    }
    return categories.insert_one(category_data)


def add_user(first_name, last_name, email, password, role):
    user_data = {
        'First Name': first_name,
        'Last Name': last_name,
        'Email': email,
        'Password': password,
        'Role': role,
        'Date Added': datetime.datetime.now(),
        'Date Modified': datetime.datetime.now()
    }
    return users.insert_one(user_data)


def add_recipe(recipe_name, category, ingredients, preparation, notes, first_name, last_name):
    recipe_data = {
        'Recipe Name': recipe_name,
        'Category': category,
        'Ingredients': ingredients,
        'Preparation': preparation,
        'Notes': notes,
        'First Name': first_name,
        'Last Name': last_name,
        'Date Added': datetime.datetime.now(),
        'Date Modified': datetime.datetime.now()
    }
    return recipes.insert_one(recipe_data)


def initial_database():
    # add roles
    admin = add_role('admin')
    contributor = add_role('contributor')
    user = add_role('user')

    # add users
    mike = add_user('Mike', 'Colbert', 'mike@mike.com', 'abc123', 'admin')

    # add categories
    main = add_category('Main dishes')
    drink = add_category('Drinks')
    desserts = add_category('Desserts')

   
    # add recipe
    chicken_parmesean = add_recipe('Chicken Parmesean', 'Main dishes',
                                   'chicken', 'cook it good', 'cook it real good', 'Mike', 'Colbert')


def main():
    initial_database()
   

main()
