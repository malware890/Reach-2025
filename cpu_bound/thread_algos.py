import threading
import time


class NoteThread:
    def __init__(self, thread: threading.Thread, note: int):
        self.thread = thread
        self.note = note


def fcfs(thread_queue):
    for thread in thread_queue:
        print(f"Starting thread {thread.thread.name}")
        thread.thread.start()
        thread.thread.join()
        print(f"Thread {thread.thread.name} Completed")


def sjf(threads: list[NoteThread]):
    threads = list(sorted(threads, key=lambda t: t.note))
    for thread in threads:
        print(f"Starting thread {thread.thread.name}")
        thread.thread.start()
        thread.thread.join()
        print(f"Thread {thread.thread.name} Completed")


def ljf(threads: list[NoteThread]):
    threads = list(sorted(threads, key=lambda t: t.note, reverse=True))
    for thread in threads:
        print(f"Starting thread {thread.thread.name}")
        thread.thread.start()
        thread.thread.join()
        print(f"Thread {thread.thread.name} Completed")


def priority_schedule(threads: list[NoteThread]):
    threads = list(sorted(threads, key=lambda t: t.note))
    for thread in threads:
        print(f"Starting thread {thread.thread.name}")
        thread.thread.start()
        thread.thread.join()
        print(f"Thread {thread.thread.name} Completed")

def rr(threads: list[NoteThread], quantum: int):
    for note_thread in threads:
        note_thread.thread.start()

    while any(note_thread.thread.is_alive() for note_thread in threads):
        for note_thread in threads:
            if note_thread.thread.is_alive():
                print(f"Running thread: {note_thread.thread.name}")
                time.sleep(quantum)
                if not note_thread.thread.is_alive():
                    print(f"Thread {note_thread.thread.name} Completed")

def mlq(threads: list[NoteThread]):
    threads = list(sorted(threads, key=lambda t: t.note))
    tri_split = len(threads) // 3

    if not len(threads) % 3:
        l1 = threads[: tri_split]
        l2 = threads[tri_split : tri_split * 2]
        l3 = threads[tri_split * 2 :]
    elif len(threads) % 3 == 1:
        l1 = threads[: tri_split + 1]
        l2 = threads[tri_split + 1 : tri_split * 2 + 1]
        l3 = threads[tri_split * 2 + 1:]
    else:
        l1 = threads[: tri_split + 1]
        l2 = threads[tri_split + 1 : tri_split * 2 + 2]
        l3 = threads[tri_split * 2 + 2 :]

    fcfs(l3)
    sjf(l2)
    rr(l1, 0.1)
