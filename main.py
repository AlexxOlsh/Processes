import multiprocessing
import time


def num_to_square(num, my_queue):
    my_queue.put(num**2)


def compute_squares(numbers):
    my_queue = multiprocessing.Queue()
    processes = []
    results = []
    for num in numbers:
        proc = multiprocessing.Process(target=num_to_square, args=(num, my_queue))
        processes.append(proc)
        proc.start()
        results.append(my_queue.get())

    for proc in processes:
        proc.join()

    return results


if __name__ == '__main__':
    print(compute_squares([1, 2, 3]))



