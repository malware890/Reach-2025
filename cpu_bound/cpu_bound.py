import sys
import os
import threading
from cpu_bound.cpu_yob_tasks import *
from cpu_bound.cpu_math import *
from cpu_bound.fashionmnist import *
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)
from thread_algos import *


maze = Maze("mazes/maze.txt")
maze2 = Maze("mazes/maze2.txt")

def mat_wrapper():
    for _ in range(5):
        mat_mult(
            [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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
    ],  [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
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

def prime_wrapper():
    for _ in range(5):
        prime_check(1, 1000000)

def dfs_wrapper():
    for _ in range(30):
        maze.dfs()
    for _ in range(30):
        maze2.dfs()

def bfs_wrapper():
    for _ in range(30):
        maze.dfs()
    for _ in range(30):
        maze2.dfs()

def nn_wrapper():
    for _ in range(9):
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

    for _ in range(30):
        model_check(knowledge, query)

mat_thread = threading.Thread(target=mat_wrapper)
prime_thread = threading.Thread(target=prime_wrapper)
dfs_thread = threading.Thread(target=dfs_wrapper)
bfs_thread = threading.Thread(target=bfs_wrapper)
nn_thread = threading.Thread(target=nn_wrapper)
mc_thread = threading.Thread(target=mc_wrapper)

sorts = [merge_sort, quick_sort, heap_sort]
yob_threads_cpu = []

for i in range(1880, 1960, 20):
    for j in range(3):
        yob_threads_cpu.append(threading.Thread(target=cpu_yob, args=(f"yobs/yob{i}.txt", sorts[j])))


threads_cpu = []
def get_cpu(algo):
    global threads_cpu
    if algo == "fcfs":
        threads_cpu = [NoteThread(thread, 0) for thread in yob_threads_cpu]
        threads_cpu += [
            NoteThread(mat_thread, 0),
            NoteThread(prime_thread, 0),
            NoteThread(dfs_thread, 0),
            NoteThread(bfs_thread, 0),
            NoteThread(nn_thread, 0),
            NoteThread(mc_thread, 0)
            ]
        fcfs(threads_cpu)
    elif algo == "sjf" or algo == "ljf":
        threads_cpu = [NoteThread(yob_threads_cpu[i], i + 5) for i in range(len(yob_threads_cpu))] + [
            NoteThread(mat_thread, 4),
            NoteThread(prime_thread, 3),
            NoteThread(dfs_thread, 1),
            NoteThread(bfs_thread, 2),
            NoteThread(nn_thread, 10000),
            NoteThread(mc_thread, 30)
        ]
        if algo[0] == "s":
            sjf(threads_cpu)
        else:
            ljf(threads_cpu)
    elif algo == "rr":
        threads_cpu = [
            NoteThread(mat_thread, 0),
            NoteThread(prime_thread, 0),
            NoteThread(dfs_thread, 0),
            NoteThread(bfs_thread, 0),
            NoteThread(nn_thread, 0),
            NoteThread(mc_thread, 2)
        ] + [NoteThread(yob_thread, 0) for yob_thread in yob_threads_cpu]
        rr(threads_cpu, 0.1)
    elif algo == "priority_schedule" or "mlq":
        threads_cpu = [NoteThread(yob_threads_cpu[i], 10 - i) for i in range(len(yob_threads_cpu))]
        threads_cpu += [
            NoteThread(mat_thread, 1),
            NoteThread(prime_thread, 0),
            NoteThread(dfs_thread, 98),
            NoteThread(bfs_thread, 80),
            NoteThread(nn_thread, 95),
            NoteThread(mc_thread, 99)
            ]
        if algo[0] == "p":
            mlq(threads_cpu)
        else:
            priority_schedule(threads_cpu)
    else:
        print("Invalid Argument: Enter a Scheduling Algorithm")
