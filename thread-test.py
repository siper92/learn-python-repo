#!/usr/bin/env python
from __future__ import print_function
import threading
import time
import math

def test():
    print('test')


class MyThread(threading.Thread):
    def run(self):
        print("{} started!".format(self.getName()))              # "Thread-x started!"
        time.sleep(1)      # Pretend to work for a second
        test()
        print("{} finished!".format(self.getName()))             # "Thread-x finished!"
 
if __name__ == '__main__':
    for x in range(4):                                     # Four times...
        mythread = MyThread(name = "Thread-{}".format(x + 1))  # ...Instantiate a thread and pass a unique ID to it
        mythread.start()                                   # ...Start the thread
        time.sleep(.9)

    images = list(range(1, 51))
    number_of_images = len(images)
    number_of_threads_to_spawn = 7
    elements_per_thread = math.ceil(number_of_images / number_of_threads_to_spawn)
    for i in range(number_of_threads_to_spawn):
        starting_index = i*elements_per_thread
        end_index = starting_index + elements_per_thread
        download_images = images[starting_index:end_index]

        if not download_images:
            continue
