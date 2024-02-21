import time
import logging
logging.basicConfig(
    level=logging.DEBUG,  # Sets the minimum log level to DEBUG
    format='%(asctime)s - %(levelname)s - %(message)s'  # Sets the log message format
)

def tictoc(func):
    def wrapper(*args, **kwargs):
        tic = time.perf_counter()
        result = func(*args, **kwargs)  # Call the function and store the result
        toc = time.perf_counter()
        logging.debug(f"{func.__name__} ran in {toc - tic:0.4f} seconds")
        return result 
    return wrapper

@tictoc
def do_this():
    time.sleep(1.3)
    return 'do_this returned'

@tictoc
def do_that(text):
    time.sleep(0.4)
    return f'do_that returned with text {text}'

if __name__ == "__main__":
    print(do_this())
    print(do_that('banana'))