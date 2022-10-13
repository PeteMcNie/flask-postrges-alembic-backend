### Flask, SQLAlchemy, Alembic, Bolierplate

#### I have not tested any of the notes or commands here yet! They are probably not quite right or completely wrong.


## Initial set up

I set up this project using Poetry to manage the dependencies. With Poetry we can lock in the versions of the packages our porject depends upon and then activate our virtual environment so that we know the project will work on anyones machine.

# Firstly
- Clone this repo onto your local machine
- Then run: `git init` (this enables git to 'know' about the project so you can commit etc)
- You will need to change the 'remote' repo the project is pointing at otherwise you will over write this boilerplate NOTE TO SELF: add commands to do this

# Poetry Commands
- Install poetry on your machine if required go to [poetry docs](https://python-poetry.org/docs/) for info on how to do this.

- `poetry --version`
- `poetry self update`
- `poetry init` or `poetry install` (not sure which one of these you will need to run if you have cloned this project)


# To run backend and see route in test blueprints file

Activate your virtual environment
1. `source $(poetry env info --path)/bin/activate` To get the path to poetry if you need it run: `poetry shell`

2. `poetry install` to install the projects dependencies

3. `FLASK_APP=app/app APP_SETTINGS=settings/development.py flask run` this sets the required environment variables and then runs the app. Read below how to get environment variables to load when you enter a directory

4. Fire up [localhost:5000/test/test-get-all] (http://127.0.0.1:5000/test/test-get-all) to check it out.

5. You can checkout all the other routes in the `test` blueprint file. The add and update routes will not work at this stage...need to set up alembic first.

Note: `deactivate` closes the virtual environment when you are finished.


# Environment variables set on load with direnv (mac)

Note: Read more about direnv [here])(https://shivamarora.medium.com/a-guide-to-manage-your-environment-variables-in-a-better-way-using-direnv-2c1cd475c8e)
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

# *You should always place the `.direnv` and `.envrc` files in your `.gitignore`*

