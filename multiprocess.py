from multiprocessing import Process
from multiprocessing import process
from multiprocessing.connection import Client
import client as Client

if __name__ == "__main__":
    count = 2
    processes = {}
    for x in range(count):
        processes[x] = Process(target=Client.run)
    for x in range(count):
        processes[x].start()

