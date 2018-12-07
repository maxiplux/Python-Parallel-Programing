from pony.orm import *
import time, datetime

import config

db = Database()
db.bind(provider=config.PROVIDER, user=config.DB_USER, password=config.DB_PASSWORD, host=config.DB_HOST,
        database=config.DB_SCHEME)


class Person(db.Entity):
    name = Required(str)
    age = Required(int)
    date = Required(datetime.datetime)

    def __str__(self):
        return "Person Name ({name}) Age({age})".format(name=self.name, age=self.age)


db.generate_mapping(create_tables=config.CREATE_TABLES)
