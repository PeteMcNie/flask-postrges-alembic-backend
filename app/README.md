### Flask, SQLAlchemy, Alembic, Bolierplate

#### I have not tested any of the notes or commands here yet! They are probably not quite right or completely wrong.


## Initial set up

I set up this project using Poetry to manage the dependencies. With Poetry we can lock in the versions of the packages our porject depends upon and then activate our virtual environment so that we know the project will work on anyones machine.

# Firstly
- Clone this repo onto your local machine
- Then run: `git init` (this enables git to 'know' about the project so you can commit etc)

# Poetry Commands
- Install poetry on your machine if required go to [poetry docs](https://python-poetry.org/docs/) for info on how to do this.

- `poetry --version`
- `poetry self update`
- `poetry init` or `poetry install` (not sure which one of these you will need to run if you have cloned this project)

To activate/deactivate virtual environment
1. `source $(poetry env info --path)/bin/activate` To get the path to poetry if you need it run: `poetry shell`

2. `deactivate`


# To run backend and see route in test blueprints file

- You need to have activated your virtual environment as mentioned above in Poetry commands
- Then steps to run here...
- Fire up [localhost:5000/test/test-get-all] (http://127.0.0.1:5000/test/test-get-all) to check it out

