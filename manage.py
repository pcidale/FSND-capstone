from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from api import create_api

api, migrate = create_api()
manager = Manager(api)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
