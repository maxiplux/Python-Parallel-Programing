import threading
import time
from multiprocessing import Pool, Process

import config
import controller


def write_row(line, multi_pool=True):
    # if multi_pool:
    #     print("processing a single line Multi Pool")
    # else:
    #     print("processing a single line in Threads")

    line = str(line).split(";")
    if len(line) != 1:
        name, age = line[0].replace('"', ''), line[1].replace("'", "")

        controller.add_person(name=name, age=age)


def send_row_to_db(lines):
    lines = lines.splitlines()
    for line in lines:
        write_row(line, multi_pool=False)


def send_row_to_db_multi_thread_pool(lines):
    t0 = time.time()
    lines = lines.splitlines()
    # the value here when we are working with db , is critical because we cool add overload to db  by number of connections
    pool = Pool(config.POOL_PROCESS)  # how many thread will be write on same time on db
    pool.map(write_row, lines)
    print("Time Elepase  {time} pool  thread ".format(time=round(t0 - time.time(), 3)))


def working_single_thread():
    print("Workin single thread ")
    t0 = time.time()
    files_to_process = controller.read_file_to_list()
    for file in files_to_process:
        send_row_to_db(file)
    print("Time Elepase  {time} single thread".format(time=round(t0 - time.time(), 3)))


def working_multi_thread():
    print("Workin multi threadingn simple")
    t0 = time.time()
    files_to_process = controller.read_file_to_list()
    for file in files_to_process:
        threading.Thread(target=send_row_to_db, args=[file]).start()  # <- 1 element list
    print("Time Elepase  {time} Multi Thread wait , we are working on other threads".format(
        time=round(t0 - time.time(), 3)))


def working_multi_thread_pool():
    print("Workin multi threadingn POOL threads")
    t0 = time.time()
    files_to_process = controller.read_file_to_list()
    for sub_file in files_to_process:
        send_row_to_db_multi_thread_pool(sub_file)
    print("Time Elepase  {time} Multi Thread".format(time=round(t0 - time.time(), 3)))


def working_multi_process():
    print("Workin multi process   ")
    t0 = time.time()
    files_to_process = controller.read_file_to_list()
    for file in files_to_process:
        p = Process(target=send_row_to_db, args=(file,))
        p.start()
        p.join()
    print("Time Elepase  {time} Multi Thread wait , we are working on other process".format(time=round(t0 - time.time(), 3)))

def main(option="single"):
    t0 = time.time()
    options = {
        "single": working_single_thread,
        "thread": working_multi_thread,
        "pool": working_multi_thread_pool,
        "multi": working_multi_process,
    }
    if option in options:
        options[option]()
    else:
        raise ("Please , select a option  from next list single thread multi")

    # firts ,  I took the file and split on a set to send to other process
    # the number of  parts to split it , you could check on PART_OF_DATA over config.py
    print("Time on main  {time}".format(time=round(t0 - time.time(), 3)))


main(option="thread")
