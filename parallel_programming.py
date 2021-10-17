import functools
from hypersphere import hypersphere as hp
from time import perf_counter as pc
import concurrent.futures as future
import functools
def multiprocessing():
    p = []
    r = 0

    start = pc()
    with future.ProcessPoolExecutor() as  ex:
        for i in range(10):
            p.append(ex.submit(hp,1000000,11))
        for i in range(10):
            p[i].result()

    end = pc()
    print(f"Process with multiprocessing took {round(end-start, 2)} seconds")

    start = pc()
    hp(10000000,11)
    end = pc()
    print(f"Process took {round(end-start, 2)} seconds")

if __name__ == "__main__":
    multiprocessing()