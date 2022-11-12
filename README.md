# Flask, SQLAlchemy, Alembic - Bolierplate

#### I have not tested any of the notes or commands here yet! They are probably not quite right or completely wrong.


## To copy this backend boilerplate

- `git clone <url from github>`
- `rm -rf .git` to remove git files
- `git remote -v` check that there is no remote for the project you cloned this one from (check you are not going to overwrite this project!)
- `git init` to start your new project
- `git add/commit` as required
- `git remote add origin <url from github>`
- `git push -u origin main` to add project to github

*************************

## Initial set up

I set up this project using Poetry to manage the dependencies. With Poetry we can lock in the versions of the packages our porject depends upon and then activate our virtual environment so that we know the project will work on anyones machine.

### To run backend and see routes in test blueprints file

- You will need to install poetry if you haven't already
- To install poetry on your machine if required go to [poetry docs](https://python-poetry.org/docs/) for info on how to do this. To check if you have poetry installed already try and run `poetry --version`

Activate your virtual environment
1. `source $(poetry env info --path)/bin/activate` To get the path to poetry if you need it run: `poetry shell`

2. `poetry install` to install the projects dependencies

3. `FLASK_APP=app/app APP_SETTINGS=settings/development.py flask --debug run` this sets the required environment variables and then runs the app. Read below how to get environment variables to load when you enter a directory so that you only need to run `flask --debug run` instead.

4. Fire up [localhost:5000/test/test-get-all](http://127.0.0.1:5000/test/test-get-all) to check it out.

5. You can checkout all the other routes in the `test` blueprint file. The add and update routes will not work at this stage...need to set up alembic first.

Note: `deactivate` closes the virtual environment when you are finished.


### Environment variables set on load with direnv (mac)

Note: Read more about direnv [here](https://shivamarora.medium.com/a-guide-to-manage-your-environment-variables-in-a-better-way-using-direnv-2c1cd475c8e)
1. Install direnv if you haven't already `brew install direnv`

2. Add this line to your ~/.bashrc or ~/.bash_profile file `eval "$(direnv hook bash)"`

3. Go into directory you would like environemnt variables set in and create a `.envrc` file

4. Set an environment variable in the `.envrc` file eg: `export MY_NAME=pete`

5. Exit the directory you have placed the `.envrc` file in eg `cd ..`

6. Re-enter that directory you just left, the terminal should display a `direnv` error blocking the environment variable from loading. This is for security. Seen as we know about the variable.

7. `direnv allow` you will see your variable load when you enter the directory. To test run `echo $MY_NAME` in the terminal...your variable should be printed.

8. 
a) Everytime you update the `.envrc` file you will have to run `direnv allow` again unless you follow step 8 b).

b) `direnv edit` opens an editor for you to make changes to the `.envrc` file. Once you've made the changes and closed the file they will be live without you having to run `direnv allow` again. 

Note: To make VSCode open when you run `direnv edit` place `export EDITOR="code --wait"` in your `~/.bashrc` or `~/.bash_profile` file.

#### *You should always place the `.direnv` and `.envrc` files in your `.gitignore`*


*************************

## Datebase setup

### Postgres

See 'Postgres set up' below if you need to set up a new database and link your project to this new datbase.

To access a postgres database you have already linked to your project use the commands below in your terminal:

- `psql <database_name>` - accesses your database via the terminal
- `psql` - defaults to the default database for your postgres
- `\dt` - lists all tables in your database
- `crtl d` - exits postgres in your terminal


### Postgres set up

You will need to set up postgres on your machine and create a new database. You will then reference this database in the setting.development.py and almebic.ini files so that the backend and talk to the correct database.

See the [postgres docs](https://www.postgresql.org/docs/current/) to set up a new database. Below are some common commands that you can run in your terminal.

- `createdb` - yup, it's that easy this will default to the name of your terminal/machine. If this name is already taken it won't work.
- `createdb <new_db_name_here>` - that's better
- `dropdb <db_name_you_want_to_remove>` - to get rid of a db you don't want
- `psql <database_name>` - accesses your database via the terminal


*************************

## Accessing your database from your python project

### Alembic set up

Note: If cloning this repo to use. At this point you should decide what table/s you actually want and alter the models file so that your project does not end up with the test_table in it.

Note: You may need to delete the alembic files committed here already and then follow these instructions to get alembic set up for your migrations.

1. `poetry run alembic init ./alembic` 

2. Inside `alembic.ini` update the `sqlalchemy.url` line to include the db url that is in the development.py file under SQLALCHEMY_DATABASE_URI. Note: in the `almebic.ini` file you do not enter the variable as a string.

3. Update `alembic/env.py` file `target_metadata` line. You need to import your db and use your dbs target_metadata. The lines should be something like this:

`
from model import db
target_metadata = [db.metadata]
`

4. `alembic revision --autogenerate -m '<An alembic revision message here>'` this generates the alembic revision file.

Note: If this doesn't work you mean need to check if an `alembic_version` table exists already in your db. If so, you can delete this so that you can run your first alembic migration.

5. `alembic upgrade head` runs the revision file. 

6. Add new tables or modify current tables and then run steps 4 and 5 again as requried. If you need to rollback an update to your database you can run `alembic downgrade -1`. This reverts your last upgrade so you can make changes if required.

*************************

## Formatters: Black, mypy etc

To run the different formatters in your terminal make sure you have first activated your virtual environment then follow the steps below based on the formatter/service you require:

- Black: formats python code. Run: `black .`
- mypy: type-checks python code. Run `mypy .`
- isort: orders your import statements. Run `isort.`

Note: bandit, flake8 and pylint are also included in this project but I have not run these yet.
