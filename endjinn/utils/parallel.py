import multiprocessing


def get_num_cores():
    return multiprocessing.cpu_count()


