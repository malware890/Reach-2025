import threading
from thread_algos import *
from dbms import *
from yobs_proc import *
from cpu_math import *
from fashionmnist import *
# from ftp import *
# from http import *

maze = Maze("maze.txt")
db = DBMS("runner.json")

def mat_wrapper():
    for i in range(9):
        mat_mult([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ], [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ])
    print(mat_mult([
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ],[
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    ]))

def prime_wrapper():
    for i in range(9):
        prime_check(1, 1000000)
    print(prime_check(1, 1000000))

def dfs_wrapper():
    for i in range(9):
        maze.dfs()
    print(maze.dfs())

def bfs_wrapper():
    for i in range(9):
        maze.bfs()
    print(maze.bfs())

def nn_wrapper():
    for i in range(5):
        neural_network()
    overall_accuracy, overall_accuracy2, overall_training_accuracy = neural_network()
    print(f"Overall Test Accuracy: {overall_accuracy:3.1f}%")
    print(f"Overall Validation Accuracy: {overall_accuracy2:3.1f}%")
    print(f"Overall Training Accuracy: {overall_training_accuracy:3.1f}%")

def mc_wrapper():
    R = Symbol("R")
    S = Symbol("S")
    W = Symbol("W")
    H = Symbol("H")
    C = Symbol("C")
    P1 = Symbol("P1")
    P2 = Symbol("P2")
    P3 = Symbol("P3")
    PG = Symbol("PG")
    A1 = Symbol("A1")
    A2 = Symbol("A2")
    A3 = Symbol("A3")
    E1 = Symbol("E1")
    E2 = Symbol("E2")
    E3 = Symbol("E3")

    knowledge = And(
        Implication(R, Symbol("W1")),
        Implication(And(S, H), E3),
        Implication(Or(C, W), Not(P1)),
        Implication(And(Symbol("W1"), Not(C)), P2),
        Implication(And(P1, P2), P3),
        Biconditional(PG, Or(P1, P2, P3)),
        Implication(E2, Not(A1)),
        Implication(E3, And(A2, A3)),
        Implication(And(R, Not(E1)), E2),
        Implication(Or(E1, E2), Not(P3)),
        Implication(E3, E1),
        Implication(A1, Not(A3)),
        Implication(Not(E2), H),
        Biconditional(A2, Or(S, Not(H))),
        Implication(C, And(Not(R), W)),
        Implication(W, Or(E1, E3)),
        Implication(Not(PG), And(Not(P1), Not(P2), Not(P3))),
        Implication(And(A3, H), S),
        Biconditional(E1, Not(Symbol("W1"))),
        Implication(Symbol("W1"), Not(A1)),
        Implication(A2, Not(E2)),
        Implication(And(A1, Not(A2)), C)
    )

    query = Implication(PG, Or(A1, A2, A3))

    for i in range(14):
        model_check(knowledge, query)
    print(model_check(knowledge, query))

def db_wrapper():
    for i in range(20):
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


mat_thread = threading.Thread(target=mat_wrapper)
prime_thread = threading.Thread(target=prime_wrapper)
dfs_thread = threading.Thread(target=dfs_wrapper)
bfs_thread = threading.Thread(target=bfs_wrapper)
nn_thread = threading.Thread(target=nn_wrapper)
mc_thread = threading.Thread(target=mc_wrapper)
# ftp_thread = threading.Thread(target=run_ftp)
# http_thread = threading.Thread(target=run_http)

sorts = [selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort]
yob_threads = []

for i in range(1880, 1960, 20):
    for j in range(5):
        yob_threads.append(threading.Thread(target=yob_process, args=(f"yobs/yob{i}.txt", sorts[j], f"yob_outputs/wyob{i}.txt")))

threads = [NoteThread(thread, 0) for thread in yob_threads]
# threads += [NoteThread(mat_thread, 0),
#             NoteThread(prime_thread, 0),
#             NoteThread(dfs_thread, 0),
#             NoteThread(bfs_thread, 0),
#             NoteThread(nn_thread, 0),
#             NoteThread(mc_thread, 0)]

if __name__ == "__main__":
    fcfs(threads)
