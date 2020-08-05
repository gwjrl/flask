from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.model.user_model import User
from app.model.new_model import *
from app import create_app, db

app = create_app('develop')

manage = Manager(app=app)
migrate = Migrate(app=app, db=db)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()