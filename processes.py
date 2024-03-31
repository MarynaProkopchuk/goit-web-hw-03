
from multiprocessing import Pool, current_process, cpu_count
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def factorize(*number):
    logging.info(f"start process {current_process().name}: {number}")
    for num in number:
        lst=[]
        for n in range(num):
            n+=1
            if num%n==0:
                lst.append(n)
        logging.info(f"result {current_process().name}: {lst}")
        return lst

if __name__ == '__main__':
    with Pool(processes=3) as pool:
        logging.info(pool.map(factorize, (128, 255, 99999, 10651060)))
        