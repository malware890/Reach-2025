import threading
import time


class NoteThread:
    def __init__(self, thread: threading.Thread, note: int):
        self.thread = thread
        self.note = note


def fcfs(thread_queue):
    for thread in thread_queue:
        thread.thread.start()
        thread.thread.join()


def sjf(threads: list[NoteThread]):
    threads = list(threads)
    while threads:
        shortest = 0
        for i in range(len(threads)):
            if threads[i].note < shortest:
                shortest = i
        thread = threads.pop(shortest)
        thread.thread.start()
        thread.thread.join()


def ljf(threads: list[NoteThread]):
    threads = list(threads)
    while threads:
        longest = 0
        for i in range(len(threads)):
            if threads[i].note > longest:
                longest = i
        thread = threads.pop(longest)
        thread.thread.start()
        thread.thread.join()


def priority_schedule(threads: list[NoteThread]):
    threads = list(threads)
    while threads:
        importantest = -1
        for i in range(len(threads)):
            if threads[i].note > importantest:
                importantest = i
        thread = threads.pop(importantest)
        thread.thread.start()
        thread.thread.join()
