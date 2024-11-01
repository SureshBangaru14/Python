import multiprocessing

from multiprocessing import Process


def do_work():
    print("Start Work")
    i = 0
    for _ in range(20000000):
        i+=1

    print("Finsihed Work")


if __name__ == "__main__":
    multiprocessing.set_start_method("spawn")
    for _ in range(5):
        p = Process(target=do_work, args=())
        p.start()