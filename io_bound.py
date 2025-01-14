import threading
import time
from thread_algos import *
from dbms import *
from yobs_proc import io_yob
from ftp import run_ftp
from http import run_http


db = DBMS("runner.json")
def db_wrapper():
    for _ in range(20):
        db.insert({"id": 1, "name": "Alice", "age": 25})
        db.insert({"id": 2, "name": "Bob", "age": 30})
        db.insert({"id": 3, "name": "Charlie", "age": 35})
        db.select()
        db.select(lambda record: record["age"] > 25)
        db.update(lambda record: record["id"] == 2, lambda record: record.update({"name": "Bobby"}))
        db.delete(lambda record: record["id"] == 3)
        db.insert({"id": 4, "name": "Diana", "age": 28})
        db.insert({"id": 5, "name": "Eve", "age": 22})
        db.select()
        db.update(lambda record: record["age"] < 30, lambda record: record.update({"status": "young"}))
        db.delete(lambda record: record["age"] > 30)
        db.insert({"id": 6, "name": "Frank", "age": 27})
        db.insert({"id": 7, "name": "Grace", "age": 24})
        db.select(lambda record: "status" in record)
        db.update(lambda record: record["id"] == 1, lambda record: record.update({"name": "Alicia"}))
        db.delete(lambda record: record["id"] == 5)
        db.insert({"id": 8, "name": "Hank", "age": 31})
        db.select(lambda record: record["name"].startswith("A"))
        db.update(lambda record: record["id"] == 6, lambda record: record.update({"age": 28}))
        db.delete(lambda record: record["id"] == 8)
        db.insert({"id": 9, "name": "Ivy", "age": 26})
        db.insert({"id": 10, "name": "Jack", "age": 29})
        db.select(lambda record: record["id"] > 5)
        db.update(lambda record: record["age"] == 29, lambda record: record.update({"age": 30}))
        db.delete(lambda record: record["id"] == 7)
        db.insert({"id": 11, "name": "Karen", "age": 32})
        db.select(lambda record: record["age"] >= 30)
        db.update(lambda record: record["id"] == 9, lambda record: record.update({"status": "updated"}))
        db.delete(lambda record: record["name"] == "Karen")
        db.insert({"id": 12, "name": "Liam", "age": 21})
        db.insert({"id": 13, "name": "Mia", "age": 23})
        db.select(lambda record: record["id"] % 2 == 0)
        db.update(lambda record: record["name"] == "Liam", lambda record: record.update({"age": 22}))
        db.delete(lambda record: record["name"] == "Mia")
        db.insert({"id": 14, "name": "Noah", "age": 33})
        db.select(lambda record: record["age"] > 20)
        db.update(lambda record: record["id"] == 14, lambda record: record.update({"age": 34}))
        db.delete(lambda record: record["id"] == 12)
        db.insert({"id": 15, "name": "Olivia", "age": 29})
        db.select(lambda record: record["name"].startswith("O"))
        db.update(lambda record: record["id"] == 15, lambda record: record.update({"name": "Liv"}))
        db.delete(lambda record: record["id"] == 11)
        db.insert({"id": 16, "name": "Paul", "age": 36})
        db.insert({"id": 17, "name": "Quinn", "age": 27})
        db.select(lambda record: record["age"] < 30)
        db.update(lambda record: record["id"] == 17, lambda record: record.update({"status": "active"}))
        db.delete(lambda record: record["id"] == 16)
        db.insert({"id": 18, "name": "Rachel", "age": 31})


dbms_thread = threading.Thread(target=db_wrapper)
ftp_thread = threading.Thread(target=run_ftp)
http_thread = threading.Thread(target=run_http)


yob_threads_io = []

for i in range(1880, 2024, 20):
    yob_threads_io.append(threading.Thread(target=io_yob, args=(f"yobs/yob{i}.txt")))
yob_threads_io.append(threading.Thread(target=io_yob, args=(f"yobs/yob2023.txt")))


threads_io = []
def get_io(algo):
    global threads_cpu
    match algo:
        case "fcfs":
            threads_io = [NoteThread(thread, 0) for thread in yob_threads_io] + [
                NoteThread(dbms_thread, 0),
                NoteThread(ftp_thread, 0),
                NoteThread(http_thread, 0)
            ]
        case "sjf":
            threads_io = [NoteThread(yob_threads_io[i], i + 4) for i in range(len(yob_threads_io))] + [
                NoteThread(dbms_thread, 0),
                NoteThread(ftp_thread, 0),
                NoteThread(http_thread, 0)
            ]
        case "ljf":
            threads_io = [NoteThread(yob_threads_io[i], i + 4) for i in range(len(yob_threads_io))] + [
                NoteThread(dbms_thread, 0),
                NoteThread(ftp_thread, 0),
                NoteThread(http_thread, 0)
            ]
        case "rr":
            threads_io = [
                NoteThread(dbms_thread, 0),
                NoteThread(ftp_thread, 0),
                NoteThread(http_thread, 0)
            ] + [NoteThread(yob_thread, 0) for yob_thread in yob_threads_io]
        case "priority_schedule":
            threads_io = [NoteThread(yob_threads_io[i], 6 - i) for i in range(len(yob_threads_io))] + [
                NoteThread(dbms_thread, 0),
                NoteThread(ftp_thread, 0),
                NoteThread(http_thread, 0)
                ]
        case _:
            print("Invalid Argument: Enter a Scheduling Algorithm")

# ftp_thread = threading.Thread(target=run_ftp)
# http_thread = threading.Thread(target=run_http)
