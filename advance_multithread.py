# Manage Thread Pool
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


# def print_number(number): 
#     time.sleep(1)
#     return f'Number: {number}'

# numbers = [1,2,3,4,5,6,51,61,7,4,3,7,8,3,34,1,41,7,43,326,74323,115,2,41,5,6,7,4,3,4,1,2,3,1,7]

# with ThreadPoolExecutor(max_workers=6) as executor: 
#     results = executor.map(print_number, numbers, chunksize=5)

# for result in results: 
#     print(result)


def square_number(number): 
    time.sleep(2.2)
    return number * number

if __name__ == '__main__':
    numbers = [1,23,16,7,43,8345,4234,75,41,2,22,2,4,5125125,251515,633444,555,622231,5556324,1231,4124,3123,567,77854,4178884,1614124]

    with ProcessPoolExecutor(max_workers=2) as process: 
        try:
            results = process.map(square_number, numbers, timeout=2.2)
        except TimeoutError as e: 
            print(f'Timeout can not create process {str(e)}')
    for result in results: 
        print(result)