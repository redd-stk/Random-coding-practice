# multiprocesing = running tasks in parralel in different cpu cores bypassing gil

from multiprocessing import *
import time
from typing import Counter


def counter(num):
    count = 0
    while count < num:
        count += 1




def main():
    a = Process(target=counter, args=(1000000000000))
    a.start()


if __name__ == '__main__':
    main()