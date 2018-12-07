import os

from pony.orm import db_session, select, delete

import config
from model import Person
import datetime

@db_session
def add_person(name=None, age=None):
    person = Person(name=name, age=age,date=datetime.datetime.now())
    return person


@db_session
def get_persons():
    return select(p for p in Person).order_by(Person.name)


@db_session
def get_persons():
    return delete(p for p in Person)


def read_file_to_list():
    dat = []
    size = os.path.getsize(config.DATA_PATH)
    file = open(config.DATA_PATH, 'rb')
    for piece in range(config.PART_OF_DATA - 1):
        dat.append(file.read(size // config.PART_OF_DATA + 1))
    dat.append(file.read())
    file.close()
    return dat
